#!/usr/bin/env Rscript


#solutionDir <-  '/data2/test/lohhla_test/Test_620V2/solutions/'
#solutionDir <-  '/data2/test/lohhla_test/Test_620V3/solutions/'

args=commandArgs(T)
solutionDir <-  args[2]

sampleInfo <- read.table(args[1], sep='\t', header=TRUE, stringsAsFactors=FALSE)

strList <- list()
con <- 'test_lohhla.sh'
for (r in 1:nrow(sampleInfo)){
    info <- sampleInfo[r,]
    if (file.exists(as.character(info[3])) & dir.exists(as.character(info[4])) & dir.exists(as.character(info[5]))){

        type <- strsplit(as.character(info[6]), '__')[[1]][2]
        commands <- paste0( "lohhla --patientId=", as.character(info[1]),  " \\\n",
"--outputDir=" , as.character(info[2]) ," \\\n",
"--normalBAMfile=" , as.character(info[3]), " \\\n" ,
"--BAMDir=" , as.character(info[4]), " \\\n",
"--hlaPath=", as.character(info[5]), "/hlas_", type," \\\n",
"--HLAfastaLoc=" , as.character(info[5]), "/types_", type, ".fa \\\n",
"--CopyNumLoc=" , solutionDir, as.character(info[1]),  "_solutions.txt \\\n",
"--mappingStep=TRUE \\
--minCoverageFilter=5 \\
--numMisMatch=1 \\
--fishingStep=TRUE \\
--cleanUp=FALSE \\
--gatkDir=/root/anaconda3/share/picard-2.18.21-0/picard.jar \\
--novoDir=/root/anaconda3/bin/\n\n")
        strList[r] <- commands
    } else {
        stop("some files don't exist")
    }
}

writeLines(unlist(lapply(strList, paste, collapse=" ")), con=con, sep = "\n", useBytes = FALSE)

