#!/usr/bin/env Rscript

library(parallel)

# cluster on Windows / Linux
cores <- detectCores(logical = FALSE)
cl <- makeCluster(24)

base <- 2
clusterExport(cl, 'base')

res1.p <- parLapply(cl, 1: 200, function(x) { base^x })

stopCluster(cl)

for (s in res1.p){
    print(s)
}

## ref  http://www.parallelr.com/r-with-parallel-computing/
##      https://www.r-bloggers.com/how-to-go-parallel-in-r-basics-tips/
