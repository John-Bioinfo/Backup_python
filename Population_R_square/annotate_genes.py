#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse

parser = argparse.ArgumentParser(description="The USAGE")     #simplifys the wording of using argparse as stated in the python tutorial
parser.add_argument("-i", "--RSmarker", type = str, dest='testName', action='store')
# parser.add_argument("-cn", "--cook_num", type = int)
options = parser.parse_args()

refname_file = 'RS_id_genes.txt'

d = {}
f_handle = open(refname_file, 'r')
for line in f_handle:
    x = line.rstrip().split('\t')
    d[x[0]]  =  x[2]

f_handle.close()

geneS    = {}
hs       = open(options.testName,  'r')
for line in hs:
    hx = line.rstrip().split('\t')
    r1 = hx[0]
    r2 = hx[1]
    if float(hx[3]) >=0.4:
        gene1 = d.get(r1, '-')
        gene2 = d.get(r2, '-')
        geneS[r1 +'\t' + r2] = gene1+'/'+gene2
        #print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(hx[0], d.get(r1, '-'), hx[1], d.get(r2, '-'), hx[2], hx[3]))
hs.close()


for i in geneS:
    pairGenes = geneS[i]
    x = pairGenes.split('/')
    ## if pair RS id corresponding Gene is not the same , output
    if pairGenes.find('-') != -1 or x[0] != x[1]:
        print('{0}\t{1}'.format(i, geneS[i]))


