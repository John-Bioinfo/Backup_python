
samples=(091 092 093 094 095 096)

for rnaS in ${samples[@]} 
do
    #cutadapt -a CGGAAGCACCAGGAGCTG$ -e 0.3 --no-trim -o ./results/cutOUT_S091_ALK.fq --untrimmed-output untrimTMP.fq ./data/S091.fq
    cutadapt -a TGTACCGCCGGAAGCACCAGGAGCTG$ -e 0.35 --no-trim -o ./results/cutOUT_S${rnaS}_ALK.fq --untrimmed-output untrimTMP.fq ./data/S${rnaS}.fq > ./results/cut_${rnaS}_ALK.log
    cutadapt -a CTGGAGTCCCAAATAAACCAGGCATT$ -e 0.35 --no-trim -o ./results/cutOUT_S${rnaS}_ROS1.fq --untrimmed-output untrimTMP.fq ./data/S${rnaS}.fq > ./results/cut_${rnaS}_ROS1.log

    awk 'NR %2 {print} !(NR%2) {print substr($0, 0, length($0)-28)}' ./results/cutOUT_S${rnaS}_ALK.fq > ./results/subcut_S${rnaS}_ALK.fq
    awk 'NR %2 {print} !(NR%2) {print substr($0, 0, length($0)-28)}' ./results/cutOUT_S${rnaS}_ROS1.fq > ./results/subcut_S${rnaS}_ROS1.fq

    /thinker/dstore/r3data/qiaozy2/bwa-0.7.13/bwa mem -R "@RG\tID:SR\tSM:NGS\tPL:Proton" -p -t 8 -T 15 EML4.fa ./results/subcut_S${rnaS}_ALK.fq > ./results/subcut_EML4_${rnaS}.sam 2>>align2_${rnaS}.log
    /thinker/dstore/r3data/qiaozy2/bwa-0.7.13/bwa mem -R "@RG\tID:SR\tSM:NGS\tPL:Proton" -p -t 8 -T 15 SLC34A2.fa ./results/subcut_S${rnaS}_ROS1.fq > ./results/subcut_SLC34A2_${rnaS}.sam 2>>align2_${rnaS}.log

    #echo -ne "${rnaS}\tALK-EML4\t"
    #awk '{if($3=="EML4")print;}' ./results/subcut_EML4_${rnaS}.sam | wc -l
    #echo -ne "${rnaS}\tROS1-SLC34A2\t"
    awk '{if($3=="SLC34A2")print $1"\t"$10;}' ./results/subcut_SLC34A2_${rnaS}.sam > ./results/subcut_SLC34A2_${rnaS}.txt
    #awk '{if($3=="EML4" && $6~/[0-9]+S$/){match($6, /[0-9]+S$/);print $1"\t"$6"\t"substr($6, RSTART, RLENGTH-1)}}' ./results/subcut_EML4_091.sam | less -S

    awk '{if($3=="EML4" && $6~/[0-9]+S$/){match($6, /[0-9]+S$/);mlen=substr($6, RSTART, RLENGTH-1);if(mlen>20){print $1"\t"$10}}}' ./results/subcut_EML4_${rnaS}.sam > ./results/subcut_EML4_${rnaS}_withintron.txt
    python pick_EML4_noIntron.py ./results/subcut_EML4_${rnaS}_withintron.txt ./results/subcut_EML4_${rnaS}.sam > ./results/subcut_EML4_${rnaS}_nointron.txt

    python createHistogram.py ./results/subcut_EML4_${rnaS}_withintron.txt ./results/subcut_EML4_${rnaS}_withintron
    python createHistogram.py ./results/subcut_EML4_${rnaS}_nointron.txt ./results/subcut_EML4_${rnaS}_nointron
    python createHistogram.py ./results/subcut_SLC34A2_${rnaS}.txt ./results/subcut_SLC34A2_${rnaS}

    ALKMap=$(wc -l ./results/cutOUT_S${rnaS}_ALK.fq)
    ROS1Map=$(wc -l ./results/cutOUT_S${rnaS}_ROS1.fq)

    EMLIntNum=$(wc -l ./results/subcut_EML4_${rnaS}_withintron.txt)
    EMLNoIntNum=$(wc -l ./results/subcut_EML4_${rnaS}_nointron.txt)
    SLCNum=$(wc -l ./results/subcut_SLC34A2_${rnaS}.txt)

    n1=$(echo ${ALKMap} | cut -d' ' -f 1)
    echo $(echo ${n1}/4 | bc)
    n2=$(echo ${ROS1Map} | cut -d' ' -f 1)
    echo $(echo ${n2}/4 | bc)

    echo $EMLIntNum
    echo $EMLNoIntNum
    echo $SLCNum

    echo "------------------------------"
    echo "------------------------------"

done


