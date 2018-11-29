import sys

def get_ENSEMBL_data(gene,  countsFile, outputF):

    c_handle = open(countsFile, "r")
    for line in c_handle:
        if line.startswith("Ensembl_ID"):
            samples = line.strip().split("\t")[1:]

        elif line.startswith(gene):
            htseqData = line.strip().split("\t")[1:]

    d = {}
    for num, i in enumerate(samples):
        d[i] = htseqData[num]

    outRes = open(outputF, "w")

    for bar in d:

        sampleType =int( bar[-3:-1] )
        if sampleType <= 9:
            outRes.write("{0}\t{1}\t{2}\n".format(gene, d[bar], "Tumor"))
        elif sampleType >= 10 and sampleType <= 19:
            outRes.write("{0}\t{1}\t{2}\n".format(gene, d[bar], "Normal"))
        elif sampleType >=20:
            print(sampleType)
    outRes.close()
    return None


get_ENSEMBL_data("ENSG00000120217",  sys.argv[1], "outPDL1.txt")

