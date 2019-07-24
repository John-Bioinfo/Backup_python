#!/usr/bin/env Rscript

library(readxl)

p_snp_tables <- Sys.glob("../paired//*.xlsx")
single_snp_tabs <- Sys.glob("./*select.xls")

##  print(p_snp_tables)
cat("pair_file\tpair_mut_num\tsingle_file\tsingle_mut_num\tcommon_mut_n\tcommon_pair_ratio\tcommon_single_ratio\thigh_40per_germline\n") 

for (i in 1:length(p_snp_tables)) {

    dat.p <- data.frame(read_excel(p_snp_tables[i], sheet=1), stringsAsFactors=F)

    dat.p[,30] <- as.character(dat.p[,30])
    dat.p[,31] <- as.character(dat.p[,31])
    

    d_t <- dat.p[, c(12, 29, 30, 31, 1)]
    d_t <- subset(d_t, d_t[,5] >= 0.05)

    pair_res <- paste(d_t[,2], d_t[,3], d_t[,4], d_t[,1], sep='--')
    dat_single <- read.table(single_snp_tabs[i], header=T, stringsAsFactors=F, sep='\t')

    dat_single[,11] <- as.character(dat_single[,11])
    dat_single[,12] <- as.character(dat_single[,12])

    d_single <- dat_single[,c(10,11,12,25,31, 44, 6)]

    d_single[,5][d_single[,5]=='.'] <- 0
    d_single[,6][d_single[,6]=='.'] <- 0

    d_single <- subset(d_single, d_single[,5] <0.001 & d_single[,6] <0.001 & d_single[,7]>=0.05)
    #d_single <- subset(d_single, d_single[,5] <0.001 & d_single[,6] <0.001 & d_single[,7]>=0.05 & d_single[,7]<=0.4)

    single_res <- paste(d_single[,1], d_single[,2], d_single[,3], d_single[,4], sep='--')
    
    pair_N   <- length(pair_res)
    single_N <- length(single_res)

    common_N <- length(intersect(pair_res, single_res))

    germ_snps <- subset(d_single, d_single[,7] > 0.4 & !single_res %in% pair_res)
    single_com_ratio <- common_N /single_N
    pair_com_ratio   <- common_N /pair_N

    #cat(p_snp_tables[i], pair_N, single_snp_tabs[i], single_N, common_N, pair_com_ratio, single_com_ratio, '\n', sep='\t')
    cat(p_snp_tables[i], pair_N, single_snp_tabs[i], single_N, common_N, pair_com_ratio, single_com_ratio, nrow(germ_snps) , '\n', sep='\t')
    #print(paste0(p_snp_tables[i], ':', as.character(length(pair_res)), '    ', single_snp_tabs[i], ':', as.character(length(single_res)) ,'  common_mut  ' , as.character(length(intersect(pair_res, single_res)))) )
    

}
