
echo start Analysis at `date`


export PATH=/thinker/net/logs/Softwares/bowtie2-2.2.8:$PATH
export PATH=/home/raomm/Software/samtools-1.5:$PATH

/thinker/net/software/tophat-2.1.1/bin/tophat2 -p 8 -G /thinker/net/congrong/RNAseq/genes.gtf -o $3\_tophat_out /thinker/dstore/r3data/AnalysisET/Reference/Transcriptomics/Homo_sapiens/UCSC/hg19/Sequence/Bowtie2Index/genome $1 $2


echo end time at `date`

