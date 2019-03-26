#!/usr/bin/env Rscript


library(DECIPHER)

seqs <- readDNAStringSet("/data2/test/lohhla_test/hla_b_all.fa", "fasta")

DNA <- AlignSeqs(seqs)

for (i in 1:length(DNA[1][[1]])){
    list <- {}
    for (j in 1:length(DNA)){
        list[j] <- substr(as.character(DNA[j][[1]]), i,i)
    }
    
    res <- as.data.frame(table(list))
    #print(as.character(table(list)))

    v <- paste(res$list, collapse='\t')
    f <- paste(res$Freq, collapse='\t')

    out <- paste0(v,'\t',f, '\n')
    cat(out)
}

#OutF <- "hlab_exon2_Seqs.fa"
#writeXStringSet(seqs, OutF, compress=F)

