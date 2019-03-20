#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import Counter
import argparse
import gzip

parser = argparse.ArgumentParser(description="The USAGE")     #simplifys the wording of using argparse as stated in the python tutorial
parser.add_argument("-i", "--input_HapFile", action = 'store', dest='testName', required = True , help="input file") # allows input of the file for reading

parser.add_argument("-m", "--RSmarker", type = str)
# parser.add_argument("-cn", "--cook_num", type = int)
options = parser.parse_args()

t= []
xh = open(options.RSmarker,  'r')
for line in xh:
    if not line.startswith('@'):
        x = line.rstrip().split('\t')[-1]
        t.append(x)
xh.close()

print('{0}\t{1}\t{2}\t{3}\t{4}'.format("RSID", 'A_Num', 'a_Num', 'TotNum', 'GenoTypes'))
for line in gzip.open(options.testName, 'rb'):
    if not line.startswith('rs#'):
        nx = line.rstrip().split()
        if nx[0] in t:
            allGenos = nx[11:]
            ad = []

            for i in allGenos:
                for j in i:
                    ad.append(j)
            y= Counter(ad)
            resGeno = []
            alleleN = 0

            for a in y.items():
                if a[0] != 'N':
                    resGeno.append('{0}:{1}'.format(a[0], a[1]))
                    alleleN += a[1]
            print('{0}\t{1}\t{2}\t{3}'.format(nx[0],  '\t'.join(resGeno), alleleN, ','.join(allGenos)))



