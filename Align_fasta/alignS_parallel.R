#!/usr/bin/env Rscript

library(parallel)
library(DECIPHER)

seqs <- readDNAStringSet("hla_A.fa", "fasta")

DNA <- AlignSeqs(seqs)

v <- names(DNA)
getC <- function(i){
    list <- unlist(lapply(v, function(x) {as.character(DNA[x][[1]][i])}))
    return(list)
}

no_cores <- detectCores(logical = FALSE)
res1.p <- mclapply(1:length(DNA[1][[1]]), 
                     FUN =  getC, 
                     mc.cores = no_cores - 2)

for (i in res1.p){
    res <- as.data.frame(table(i))
    v <- paste(res$i, collapse='\t')
    f <- paste(res$Freq, collapse='\t')

    out <- paste0(v,'\t',f, '\n')
    cat(out)
}


