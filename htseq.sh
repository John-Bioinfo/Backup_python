htseq-count -f sam -r name -s no -a 10 -t exon -i gene_id -m union ko.bam /thinker/net/congrong/RNAseq/genes.gtf > ko_Hisatcounts_out.txt 2>ko_Hisatcounts_log.txt 
htseq-count -f sam -r name -s no -a 10 -t exon -i gene_id -m union ko_nacro.bam /thinker/net/congrong/RNAseq/genes.gtf > ko_nacro_Hisatcounts_out.txt 2>ko_nacro_Hisatcounts_log.txt 
htseq-count -f sam -r name -s no -a 10 -t exon -i gene_id -m union ko_napro.bam /thinker/net/congrong/RNAseq/genes.gtf > ko_napro_Hisatcounts_out.txt 2>ko_napro_Hisatcounts_log.txt 
htseq-count -f sam -r name -s no -a 10 -t exon -i gene_id -m union wt.bam /thinker/net/congrong/RNAseq/genes.gtf > wt_Hisatcounts_out.txt 2>wt_Hisatcounts_log.txt 

htseq-count -f bam -r name -s no -a 10 -t exon -i gene_id -m union ko_nacro_tophat_out/accepted_hits.bam /thinker/net/congrong/RNAseq/genes.gtf > ko_nacro_thcounts_out.txt 2>ko_nacro_thlog.txt 
htseq-count -f bam -r name -s no -a 10 -t exon -i gene_id -m union ko_napro_tophat_out/accepted_hits.bam /thinker/net/congrong/RNAseq/genes.gtf > ko_napro_thcounts_out.txt 2>ko_napro_thlog.txt 
htseq-count -f bam -r name -s no -a 10 -t exon -i gene_id -m union ko_tophat_out/accepted_hits.bam /thinker/net/congrong/RNAseq/genes.gtf > ko_thcounts_out.txt 2>ko_thlog.txt 
htseq-count -f bam -r name -s no -a 10 -t exon -i gene_id -m union wt_tophat_out/accepted_hits.bam /thinker/net/congrong/RNAseq/genes.gtf > wt_thcounts_out.txt 2>wt_thlog.txt 
