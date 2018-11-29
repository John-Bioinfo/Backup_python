

# /work/Software/Anaconda3-5.1.0/bin/python3 pickNoAlt.py

bwa=/work/Software/bwa-0.7.17/bwa
## $bwa index -a bwtsw hg38_ref.fa

USER1=u1

#$bwa mem -t 8 hg38_ref.fa /work/${USER1}/Project/Project_WES/RawData/N0115P/N0115P.R1.fastq.gz /work/${USER1}/Project/Project_WES/RawData/N0115P/N0115P.R2.fastq.gz > N0115P.sam 2>N0115P.log 

#$bwa mem -t 8 hg38_ref.fa /work/${USER1}/Project/Project_WES/RawData/N1140F/N1140F_L4_1.fq.gz /work/${USER1}/Project/Project_WES/RawData/N1140F/N1140F_L4_2.fq.gz > N1140F.sam 2>N1140F.log

#$bwa mem -t 8 hg38_ref.fa /work/${USER1}/Project/Project_WES/RawData/N1140M/N1140M_L4_1.fq.gz /work/${USER1}/Project/Project_WES/RawData/N1140M/N1140M_L4_2.fq.gz > N1140M.sam 2>N1140M.log

#$bwa mem -t 8 hg38_ref.fa /work/${USER1}/Project/Project_WES/RawData/N1140P/N1140P_L4_1.fq.gz /work/${USER1}/Project/Project_WES/RawData/N1140P/N1140P_L4_2.fq.gz > N1140P.sam 2>N1140P.log 


samtools=/work/Software/samtools-1.8/bin/samtools

USER2=u2

$samtools view -@ 8 -bS N0115P.sam | $samtools sort - -@ 8 -T /work/${USER2}/HLA/xHLA_test/aln_N0115P.sorted -o N0115P.bam
$samtools view -@ 8 -bS N1140F.sam | $samtools sort - -@ 8 -T /work/${USER2}/HLA/xHLA_test/aln_N1140F.sorted -o N1140F.bam
$samtools view -@ 8 -bS N1140M.sam | $samtools sort - -@ 8 -T /work/${USER2}/HLA/xHLA_test/aln_N1140M.sorted -o N1140M.bam
$samtools view -@ 8 -bS N1140P.sam | $samtools sort - -@ 8 -T /work/${USER2}/HLA/xHLA_test/aln_N1140P.sorted -o N1140P.bam

$samtools index N0115P.bam
$samtools index N1140F.bam
$samtools index N1140M.bam
$samtools index N1140P.bam


docker run -v `pwd`:`pwd` -w `pwd` humanlongevity/hla \
    --sample_id N0115P --input_bam_path N0115P.bam \
    --output_path test_N0115P


docker run -v `pwd`:`pwd` -w `pwd` humanlongevity/hla \
    --sample_id N1140F --input_bam_path N1140F.bam \
    --output_path test_N1140F


docker run -v `pwd`:`pwd` -w `pwd` humanlongevity/hla \
    --sample_id N1140M --input_bam_path N1140M.bam \
    --output_path test_N1140M


docker run -v `pwd`:`pwd` -w `pwd` humanlongevity/hla \
    --sample_id N1140P --input_bam_path N1140P.bam \
    --output_path test_N1140P





