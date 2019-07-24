#!/bin/bash

if [ ! -d "LOH_Out" ];then
    mkdir LOH_Out
fi
cd LOH_Out

mkdir Sample_1870115_bam 
mkdir Sample_1870116_bam
mkdir Sample_1870117_bam
mkdir Sample_1870113_bam
mkdir Sample_1870114_bam
mkdir Sample_1870118_bam
mkdir Sample_1870121_bam

ln -s /data2/test/lohhla_test/wes_data/bam/1870115.dup.bam Sample_1870115_bam/1870115_tumor_sorted.bam 
ln -s /data2/test/lohhla_test/wes_data/bam/1870116.dup.bam Sample_1870116_bam/1870116_tumor_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1870117.dup.bam Sample_1870117_bam/1870117_tumor_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1870113.dup.bam Sample_1870113_bam/1870113_tumor_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1870114.dup.bam Sample_1870114_bam/1870114_tumor_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1870118.dup.bam Sample_1870118_bam/1870118_tumor_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1870121.dup.bam Sample_1870121_bam/1870121_tumor_sorted.bam

ln -s /data2/test/lohhla_test/wes_data/bam/1870115.dup.bam.bai Sample_1870115_bam/1870115_tumor_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1870116.dup.bam.bai Sample_1870116_bam/1870116_tumor_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1870117.dup.bam.bai Sample_1870117_bam/1870117_tumor_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1870113.dup.bam.bai Sample_1870113_bam/1870113_tumor_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1870114.dup.bam.bai Sample_1870114_bam/1870114_tumor_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1870118.dup.bam.bai Sample_1870118_bam/1870118_tumor_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1870121.dup.bam.bai Sample_1870121_bam/1870121_tumor_sorted.bam.bai

ln -s /data2/test/lohhla_test/wes_data/bam/1821004.dup.bam Sample_1870115_bam/1821004_normal_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1821006.dup.bam Sample_1870116_bam/1821006_normal_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1821008.dup.bam Sample_1870117_bam/1821008_normal_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1821010.dup.bam Sample_1870113_bam/1821010_normal_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1821012.dup.bam Sample_1870114_bam/1821012_normal_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1821032.dup.bam Sample_1870118_bam/1821032_normal_sorted.bam
ln -s /data2/test/lohhla_test/wes_data/bam/1821038.dup.bam Sample_1870121_bam/1821038_normal_sorted.bam
 
ln -s /data2/test/lohhla_test/wes_data/bam/1821004.dup.bam.bai Sample_1870115_bam/1821004_normal_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1821006.dup.bam.bai Sample_1870116_bam/1821006_normal_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1821008.dup.bam.bai Sample_1870117_bam/1821008_normal_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1821010.dup.bam.bai Sample_1870113_bam/1821010_normal_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1821012.dup.bam.bai Sample_1870114_bam/1821012_normal_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1821032.dup.bam.bai Sample_1870118_bam/1821032_normal_sorted.bam.bai
ln -s /data2/test/lohhla_test/wes_data/bam/1821038.dup.bam.bai Sample_1870121_bam/1821038_normal_sorted.bam.bai

mkdir HLA_Fa

cp /data2/test/lohhla_test/wes_data/polysolver_results/1821004/winners.hla.txt ./HLA_Fa/1821004_hla.txt
cp /data2/test/lohhla_test/wes_data/polysolver_results/1821006/winners.hla.txt ./HLA_Fa/1821006_hla.txt
cp /data2/test/lohhla_test/wes_data/polysolver_results/1821008/winners.hla.txt ./HLA_Fa/1821008_hla.txt
cp /data2/test/lohhla_test/wes_data/polysolver_results/1821010/winners.hla.txt ./HLA_Fa/1821010_hla.txt
cp /data2/test/lohhla_test/wes_data/polysolver_results/1821012/winners.hla.txt ./HLA_Fa/1821012_hla.txt
cp /data2/test/lohhla_test/wes_data/polysolver_results/1821032/winners.hla.txt ./HLA_Fa/1821032_hla.txt
cp /data2/test/lohhla_test/wes_data/polysolver_results/1821038/winners.hla.txt ./HLA_Fa/1821038_hla.txt

mkdir solutions

cp /data2/test/lohhla_test/wes_data/solutions/1870115_solutions.txt solutions/1870115_solutions.txt
cp /data2/test/lohhla_test/wes_data/solutions/1870116_solutions.txt solutions/1870116_solutions.txt
cp /data2/test/lohhla_test/wes_data/solutions/1870117_solutions.txt solutions/1870117_solutions.txt
cp /data2/test/lohhla_test/wes_data/solutions/1870113_solutions.txt solutions/1870113_solutions.txt
cp /data2/test/lohhla_test/wes_data/solutions/1870114_solutions.txt solutions/1870114_solutions.txt
cp /data2/test/lohhla_test/wes_data/solutions/1870118_solutions.txt solutions/1870118_solutions.txt
cp /data2/test/lohhla_test/wes_data/solutions/1870121_solutions.txt solutions/1870121_solutions.txt

python ../run_lohhla.py -d HLA_Fa




