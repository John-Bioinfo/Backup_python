args = commandArgs(trailingOnly=TRUE)
library(ggplot2)

data1 <- read.table(args[1], header=F, sep="\t", stringsAsFactor=F)
geneName <- strsplit(args[1], "\\.")[[1]][1]

colnames(data1) <- c("Sample", "value", "Factor")

p1<-ggplot(data1,aes(x=Factor,y=value,fill=Factor))+geom_violin(alpha=0.7)
p2<-p1+geom_jitter(alpha=0.3,col="black",show.legend=FALSE) + labs(x=geneName, color="darkgrey") + ggtitle(geneName)

mytheme<-theme_bw()+theme(panel.grid.major= element_line(color = "white"),panel.grid.minor =element_line(color= "white"),legend.title = element_blank() , plot.title = element_text(hjust = 0.5)) 
p1 <- p1+mytheme
p2 <- p2+mytheme

ggsave(paste0("plot1",geneName, ".pdf" ), p1, width = 4.5, height = 3.6) 
ggsave(paste0("plot2",geneName, ".pdf" ), p2, width = 8.15, height = 9.5) 
