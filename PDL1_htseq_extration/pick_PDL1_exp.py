#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse

def verify_Barcode(pfile):

    td = set()
    nd = set()

    pheno = open(pfile, "r")
    for line in pheno:
        if line.startswith("submitter_id.samples"):
            continue
        else:
            px = line.strip().split("\t")
            new_neoplasm = px[54]
            person_status= px[65]

            if (new_neoplasm == "New Primary Tumor" or new_neoplasm == "Distant Metastasis") and person_status == "WITH TUMOR":
                td.add(px[0])
            elif new_neoplasm == "" and person_status == "TUMOR FREE":      
                nd.add(px[0])
    pheno.close()
    return td, nd

def get_ENSEMBL_data(gene, barcodes1, barcodes2, countsFile, outputF):
    
    c_handle = open(countsFile, "r")
    for line in c_handle:
        if line.startswith("Ensembl_ID"):
            samples = line.strip().split("\t")[1:]

        elif line.startswith(gene):
            htseqData = line.strip().split("\t")[1:]            

    d = {}
    for num, i in enumerate(samples):
        d[i] = htseqData[num]

    resT = []
    resN = []
    for bar in d:
        if bar in barcodes1:
            resT.append(float(d[bar]))
        elif bar in barcodes2:
            resN.append(float(d[bar])) 

    return resT, resN



if __name__ == "__main__":
    USAGE = """python {0} -p input_phenotype file
                          -c htseq counts file
                          -o outputFile
                          -g ensembl gene ID """.format(__file__)

    parser = argparse.ArgumentParser(description = USAGE)
    parser.add_argument("-p", "--pheno", action = "store", required = True, help = "phenotype file")
    parser.add_argument("-c", "--hs_count", action = "store", required = True, help = "HT-seq counts result file")
    parser.add_argument("-o", "--outData", action = "store", default = "counts_output.txt", help = "output filename for plotting")
    parser.add_argument("-g", "--gene", action = "store", default = "ENSG00000120217", help = "minimal standard for depth filtration")

    args = parser.parse_args()

    resTumorBar, resNormalBar = verify_Barcode(args.pheno)

    Tdata, Ndata = get_ENSEMBL_data(args.gene, resTumorBar, resNormalBar, args.hs_count, args.outData)
    for hdata in Tdata:
        print("{0}\t{1}\t{2}".format(args.gene,  hdata, "Tumor"))
    for hdata in Ndata:
        print("{0}\t{1}\t{2}".format(args.gene,  hdata, "Normal"))

