nohup bash hisat.sh /thinker/net/congrong/RNAseq/XYH/ko_napro_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/ko_napro_2.clean.fq.gz ko_napro > ko_napro_hisat2.log 2>&1 &
nohup bash hisat.sh /thinker/net/congrong/RNAseq/XYH/ko_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/ko_2.clean.fq.gz ko > ko_hisat2.log 2>&1 &
nohup bash hisat.sh /thinker/net/congrong/RNAseq/XYH/ko_nacro_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/ko_nacro_2.clean.fq.gz ko_nacro > ko_nacro_hisat2.log 2>&1 &
nohup bash hisat.sh /thinker/net/congrong/RNAseq/XYH/wt_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/wt_2.clean.fq.gz wt > wt_hisat2.log 2>&1 &


nohup bash tophat.sh /thinker/net/congrong/RNAseq/XYH/ko_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/ko_2.clean.fq.gz ko > ko_topha.log 2>&1 &
nohup bash tophat.sh /thinker/net/congrong/RNAseq/XYH/ko_napro_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/ko_napro_2.clean.fq.gz ko_napro > ko_napro_topha.log 2>&1 &
nohup bash tophat.sh /thinker/net/congrong/RNAseq/XYH/ko_nacro_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/ko_nacro_2.clean.fq.gz ko_nacro > ko_nacro_topha.log 2>&1 &
nohup bash tophat.sh /thinker/net/congrong/RNAseq/XYH/wt_1.clean.fq.gz /thinker/net/congrong/RNAseq/XYH/wt_2.clean.fq.gz wt > wt_topha.log 2>&1 &

