from Bio import SeqIO

CHRC = [ "chr1" , "chr2"  , "chr3" , "chr4",  "chr5" , "chr6" , "chr7" , "chr8" , "chr9" , "chr10" , "chr11" , "chr12"
        ,"chr13" ,  "chr14",  "chr15" , "chr16" , "chr17" , "chr18" , "chr19" , "chr20"  , "chr21" , "chr22" , "chrX" , "chrY", "chrM" ]

my_records = []

for seq_record in SeqIO.parse("/work/Database/GATK_db/hg38_RefGenome/Homo_sapiens_assembly38.fasta",  "fasta"):
    if seq_record.id in CHRC:
        my_records.append(seq_record)

SeqIO.write(my_records, "hg38_ref.fa", "fasta")




