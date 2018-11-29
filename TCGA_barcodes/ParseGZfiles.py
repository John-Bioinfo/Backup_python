
import re, os
import gzip
import numpy as np
from collections import defaultdict


def FindFile_sample(d_dir, pName):
    if not os.path.isdir(d_dir):
        sys.exit("Directory does not exist. Please check it.")
    T_files = []
    for root, dirs, files in os.walk(d_dir):
        for fr in files:
            # if fr.endswith("Depth_Result.txt"):
            if pName.find("*") != -1:
                name_s = pName.split("*")
                if fr.startswith(name_s[0]) and fr.endswith(name_s[1]):
                    f_path = os.path.join(root, fr)
                    T_files.append(f_path)
            elif fr.endswith(pName):
                f_path = os.path.join(root, fr)
                T_files.append(f_path)
    return T_files

fs = FindFile_sample("./" ,"*FPKM.txt.gz")


## open barcode file
barcodes = []

barFile = open("LUSC_barcodes.txt",  "r")
for line in barFile:
    xline = line.strip().split("\t")
    barcodes.append(xline[0][:16])
barFile.close()


Mut_UUID_set = set()
Non_UUID_set = set()
## Open UUIDs and barcodes Informations

manifestF = open("gdc_manifest.2018-11-14_LUSC.txt.map2submitterID", "r")
for line in manifestF:
    if line.startswith("cases.0"):
        continue
    else:
        fx = line.strip().split("\t")
        if fx[1] == "Primary Tumor" and fx[3].endswith("FPKM.txt.gz"):
            if fx[4] in barcodes :
                #print("Mut\t" + line.strip())
                Mut_UUID_set.add(fx[3])
            else:
                #print("Ref\t" + line.strip())
                Non_UUID_set.add(fx[3])

manifestF.close()


d_NonM = defaultdict(list)
d_Mut  = defaultdict(list)


for i in fs:
    if os.path.basename(i) in Non_UUID_set:
        #print(i)
        FN = gzip.open(i, "r")
        for line in FN:
            x = line.strip().split("\t")
            ENSG_N = x[0].split(".")[0]
            d_NonM[ENSG_N].append(float(x[1]))

        FN.close()
    elif os.path.basename(i) in Mut_UUID_set:
        #print("A_Mut\t" + i)
        FM = gzip.open(i , "r")
        for line in FM:
            x = line.strip().split("\t")
            ENSG_N = x[0].split(".")[0]
            d_Mut[ENSG_N].append(float(x[1]))

        FM.close()

np.seterr(all='raise')
d_FOLD_CHANGE = {}

outputF = "result_FC.xls" 

if not os.path.exists(outputF):
    fo = open(outputF, "w")

    for i in d_Mut:
        Non_Exp = np.mean(d_NonM[i])
        Mut_Exp = np.mean(d_Mut[i])
        try:
            d_FOLD_CHANGE[i] = Mut_Exp / Non_Exp
        #except RuntimeWarning:
        except FloatingPointError:
            d_FOLD_CHANGE[i] = "NA"
        #print("{0}\t{1}\t{2}\t{3}".format(i, Mut_Exp, Non_Exp, d_FOLD_CHANGE[i]))
        fo.write("{0}\t{1}\t{2}\t{3}\n".format(i, Mut_Exp, Non_Exp, d_FOLD_CHANGE[i]))
    fo.close()

d = {}

martFile = open("mart_export_1.txt", "r")
for line in martFile:
    if line.startswith("Gene stable"):
        continue
    else:
        x = line.strip().split("\t")
        d[x[0]] = x[6]
martFile.close()

foldNew = {}

fcFile = open("result_FC.xls","r")

for line in fcFile:
    xline = line.strip().split("\t")
    ensg = xline[0].split(".")[0]
    if xline[3] != "NA":
        #print("{0}\t{1}".format(d.get(ensg, "nul"), xline[3]))
        foldNew[d.get(ensg, "nul")] = float(xline[3])

fcFile.close()

newD = {}
for item in d.items():
    newD[item[1]] = item[0]


sortN = sorted(foldNew, key=foldNew.get, reverse=True)

MeanRatio_F = open("meanRatio.xls", "w")
for i in sortN:
    #print("{0}\t{1}\t{2}".format(i, newD.get(i, "noName"), foldNew[i]))
    MeanRatio_F.write("{0}\t{1}\t{2}\n".format(i, newD.get(i, "noName"), foldNew[i]))
MeanRatio_F.close()

ratioFile_handle = open("meanRatio.xls", "r")
outfile = open("testPlot.xls", "w")

for line in ratioFile_handle:
    rx = line.strip().split("\t")

    if float(rx[2]) >= 2 or float(rx[2]) <= 0.5:
        value_Num = 0

        FPKMvalues = d_Mut[rx[1]]
        #print(FPKMvalues)
        for v in FPKMvalues:
            if v > 0.01:
                value_Num += 1
        
        if len(FPKMvalues) > 1 and value_Num * 1.0 / len(FPKMvalues) >= 0.7 :
            outfile.write("{0}\t{1}\t{2}\n".format(rx[0], ",".join([str(i) for i in FPKMvalues]), ",".join([str(i) for i in d_NonM[rx[1]]]) ))
            
outfile.close()
outDir = "genes_Comparison"
if not os.path.exists(outDir):
    os.mkdir(outDir)
os.chdir(outDir)

os.system("cp ../testPlot.xls ./")
fplot = open("testPlot.xls", "r")
for line in fplot:
    xf = line.strip().split("\t")
    dataHandle = open(xf[0] + ".txt", "w")
    mutVs = xf[1].split(",")
    nonVs = xf[2].split(",")

    for m in mutVs:
        dataHandle.write("{0}\t{1}\t{2}\n".format(xf[0], m, "Mut"))
    for n in nonVs:
        dataHandle.write("{0}\t{1}\t{2}\n".format(xf[0], n, "Non"))
    dataHandle.close()

fplot.close()

#for i in d_FOLD_CHANGE:
#    print(i, d_FOLD_CHANGE[i])
