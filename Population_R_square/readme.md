
ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/

python pick_PopFreq.py -m genes.intervals -i MEX.hmap.gz 
python calc_R2.py -m genes.intervals -i MEX.hmap.gz > MEX_res_rsq.xls
python pick_StartEnd_accordGenes.py | sort -k 3 > RS_id_genes.txt
## python annotate_genes.py -i MEX_res_rsq.xls

for i in `ls *_res_rsq.xls`
do
    python annotate_genes.py -i ${i}
done

