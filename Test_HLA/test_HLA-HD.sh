export PATH=/work/Software/bowtie2-2.3.4.1:$PATH
export PATH=$PATH:/work/Software/hlahd.1.2.0.1/bin

USER1=u1
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N0115P/N0115P.R1.fastq.gz > N0115P_R1.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N0115P/N0115P.R2.fastq.gz > N0115P_R2.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N1140F/N1140F_L4_1.fq.gz > N1140F_R1.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N1140F/N1140F_L4_2.fq.gz > N1140F_R2.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N1140M/N1140M_L4_1.fq.gz > N1140M_R1.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N1140M/N1140M_L4_2.fq.gz > N1140M_R2.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N1140P/N1140P_L4_1.fq.gz > N1140P_R1.fastq
#gzip -dc /work/${USER1}/Project/Project_WES/RawData/N1140P/N1140P_L4_2.fq.gz > N1140P_R2.fastq

hlahd.sh -t 2 -m 100 -c 0.95 -f freq_data/ \
         N0115P_R1.fastq \
         N0115P_R2.fastq \
          /work/Software/hlahd.1.2.0.1/HLA_gene.split.txt \
                 /work/Software/hlahd.1.2.0.1/dictionary/ \
                    N0115P \
                  N0115P_estimation

hlahd.sh -t 2 -m 100 -c 0.95 -f freq_data/ \
         N1140F_R1.fastq \
         N1140F_R2.fastq \
          /work/Software/hlahd.1.2.0.1/HLA_gene.split.txt \
                 /work/Software/hlahd.1.2.0.1/dictionary/ \
                    N1140F \
                  N1140F_estimation
hlahd.sh -t 2 -m 100 -c 0.95 -f freq_data/ \
         N1140M_R1.fastq \
         N1140M_R2.fastq \
          /work/Software/hlahd.1.2.0.1/HLA_gene.split.txt \
                 /work/Software/hlahd.1.2.0.1/dictionary/ \
                    N1140M \
                  N1140M_estimation
hlahd.sh -t 2 -m 100 -c 0.95 -f freq_data/ \
         N1140P_R1.fastq \
         N1140P_R2.fastq \
          /work/Software/hlahd.1.2.0.1/HLA_gene.split.txt \
                 /work/Software/hlahd.1.2.0.1/dictionary/ \
                    N1140P \
                  N1140P_estimation
