#!/usr/bin/env python
# -*- coding: UTF-8 -*-

geneList = 'geneNames.list' 
refGene  = 'hg19_refGene.txt'

L  = []
FH = open(geneList, 'r')
for line in FH:
    L.append(line.rstrip())
FH.close()

d = {}
RH = open(refGene,  'r')
for line in RH:
    RX = line.rstrip().split('\t')

    chrN  =  RX[2]  
    txStart  = int(RX[4])
    txEnd    = int(RX[5])
    cdsStart = int(RX[6])
    cdsEnd   = int(RX[7])
    geneName = RX[12]
    if geneName in L:
        for j in range(txStart, txEnd+1):
            d[chrN + ':' + str(j)] = '\t'.join([ geneName, RX[4], RX[5], RX[6], RX[7] ] )
RH.close()

snpIntervals = 'genes.intervals'
opSNP = open(snpIntervals, 'r')
for line in opSNP:
    if not line.startswith('@'):
        xs = line.rstrip().split('\t')
        p  = xs[0] + ':' + xs[1]
        if p in d:

            print('{0}\t{1}\t{2}'.format(xs[4], p, d[p]))
        #else:
        #    print('{0}'.format(line.rstrip()))

