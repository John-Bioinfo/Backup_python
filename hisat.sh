
echo start time at `date`

/home/qiaozy/Softwares/hisat2-2.1.0/hisat2 -p 8 --dta -x /thinker/net/wangquanwei/HISAT/ucsc-hg19-indexs/ucsc.hg19 -1 $1 -2 $2 -S $3\.bam

echo end time at `date`



