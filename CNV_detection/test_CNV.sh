#!/bin/bash

function Help(){
    cat << HELP
    USAGE for this program:
        -a input normal bam
        -t tumor bam
        -o output File
HELP
    exit 0;
}

while getopts ":a:t:ho:" opt
do
        case $opt in
                a ) inputAlignedN=$OPTARG ;;
                t ) AlignedT=$OPTARG;;
                o ) outputRes=$OPTARG;;
                h ) Help;;
                ? ) echo "error"
                    exit 1;;
        esac
done

awk '{OFS="\t";print $1, $2, $3, $4, $5, $6;}' gencode.v27_annotation.bed > primary.bed
cut --output-delimiter=$'\t' -f 1-6 gencode.v27_annotation.bed > primary.bed

sort -k1,1 -k2,2n primary.bed > primary.sorted.bed
sort -k1,1 -k2,2n Illumina_pt2.bed > Illumina_pt2.sorted.bed

/home/qiaozy2/software/bedtools2/bin/intersectBed -a primary.sorted.bed -b Illumina_pt2.sorted.bed -wa -sorted > Illumina_raw.bed

~/software/bedtools2/bin/coverageBed -abam ${inputAlignedN} -b Illumina_raw.bed -d | awk '{if($NF>=500)print;}' > Ntest_normal.dep
~/software/bedtools2/bin/coverageBed -abam ${AlignedT} -b Illumina_raw.bed -d | awk '{if($NF>=500)print;}' > Ntest_tumor.dep

python CNV_norm_new.py -i Ntest_tumor.dep -c Ntest_normal.dep -rd Illumina_raw.bed > norm_new.log 2>&1
## output file name is CopyNumber_New.xls
python pick_CNVreg.py > CNV_test.xls

awk '{print $1"\t"$4"\t"$4+9"\t"$7}' CNV_test.xls > out_raw.xls
sort -k1,1 -k2,2n out_raw.xls > sorted_CNA.bed
/home/qiaozy2/software/bedtools2/bin/intersectBed -wa -wb \
    -a Illumina_raw.bed \
    -b sorted_CNA.bed \
    -sorted > raw_dep_Exons.xls

python mergeRatio.py raw_dep_Exons.xls ${outputRes}


