
from collections import defaultdict
import sys
import numpy as np

inputF = sys.argv[1]
outF   = sys.argv[2]


exons_dict = defaultdict(list)


OHandle = open("Pre_" + outF, "w")
Fh = open(inputF, "r")

for line in Fh:
    sp = line.strip().split("\t")

    k = "\t".join(sp[0:6])
    exons_dict[k].append(float(sp[9]))

Fh.close()

for exon in exons_dict:
    sortRatio = sorted(exons_dict[exon], reverse=True)
    n = len(sortRatio)
    if n>1:
        ratio_array = np.array(sortRatio[1:])
        meanR  = np.mean(ratio_array)
        stdR   = np.std(ratio_array)
    
        if  meanR > 2.5:
            OHandle.write("{0}\t{1:.4f}\n".format(exon, meanR ))
        elif  meanR > 1.5 and meanR <= 2.5 and stdR < 0.5:
            OHandle.write("{0}\t{1:.4f}\n".format(exon, meanR ))

        elif  meanR <0.8 and stdR <0.5:
            OHandle.write("{0}\t{1:.4f}\n".format(exon, meanR ))

OHandle.close()




fileIn = open("Pre_" + outF, "r")

exonR = defaultdict(list)
geneK = dict()

for line in fileIn:
    sp = line.strip().split("\t")
    geneN = sp[4]
    e = sp[5]

    r = float(sp[6])
    exonR[geneN].append(r)
    if geneN in geneK and geneK[geneN] != e:
        geneK[geneN] += ";" + e
    else:
        geneK[geneN] = e

fileIn.close()
#print(geneK)

outNew = open("F_" + outF, "w")

fileInNew = open("Pre_" + outF, "r")

for line in fileInNew:
    sp = line.strip().split("\t")
    geneN = sp[4]

    exonNum = len(geneK[geneN].split(";"))

    ratio_array = np.array(exonR[geneN])
    stdR   = np.std(ratio_array)

    if exonNum > 2 and stdR < 0.4:
        outNew.write(line)

outNew.close()
fileInNew.close()

geneD = defaultdict(list)
VarD  = defaultdict(list)

inputF = open("F_" + outF, "r")

for line in inputF:
    z = line.strip().split("\t")

    name_TransID = z[4]
    gName = z[0]+ "-" + name_TransID.split(";")[0]
    geneD[name_TransID].append(int(z[5].replace("exon","")))
    VarD[gName].append(float(z[6]))

inputF.close()

geneExonNum = defaultdict(list)

for i in geneD:
    geneName = i.split(";")[0]
    exonRange = str(min(geneD[i])) + "-" + str(max(geneD[i]))
    geneExonNum[geneName].append(exonRange)
ExonD = {}

for eg in geneExonNum:
    tmpE = 0
    tmpAexon = 0
    tmpBexon = 0
    for e in geneExonNum[eg]:
        esmall = int(e.split("-")[0])
        elarge = int(e.split("-")[1])

        if elarge - esmall > tmpE:
            tmpE = elarge - esmall
            tmpAexon = esmall
            tmpBexon = elarge
        elif elarge - esmall == tmpE and esmall == 1:
            tmpE = elarge - esmall
            tmpAexon = esmall
            tmpBexon = elarge

    ExonD[eg]= "Exon" + str(tmpAexon) + "-" + str(tmpBexon)

outFF = open(outF,"w")
outFF.write("Chr\tGene\tRegion\tType\tVAF\n")
for gene in VarD:
    geneN = gene.split("-")
    varV1 = np.mean(np.array(VarD[gene]))
    varValue = int(round(varV1*2))
    if varValue >2:
        outFF.write("{0}\t{1}\t{2}\tCNV gain\t{3:.2f}\n".format(geneN[0], geneN[1], ExonD[geneN[1]], varValue  ))
    else:
        outFF.write("{0}\t{1}\t{2}\tCNV loss\t{3:.2f}\n".format(geneN[0], geneN[1], ExonD[geneN[1]], varValue ))


outFF.close()

