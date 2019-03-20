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

def pick_AllGenos(marker_interval, hapfile):

    d = {}
    t= []
    xh = open(marker_interval,  'r')
    for line in xh:
        if not line.startswith('@'):
            x = line.rstrip().split('\t')[-1]
            t.append(x)
    xh.close()

    ind_num = 0
    for line in gzip.open(hapfile, 'rb'):
        if not line.startswith('rs#'):
            nx = line.rstrip().split()
            if nx[0] in t:
                allGenos = nx[11:]
                ind_num  = len(nx[11:])
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

                d[nx[0]] = '{0}\t{1}\t{2}'.format( '\t'.join(resGeno), alleleN, ','.join(allGenos))

    return d, ind_num
#print('{0}\t{1}\t{2}\t{3}\t{4}'.format("RSID", 'A_Num', 'a_Num', 'TotNum', 'GenoTypes'))

allD , peopleN = pick_AllGenos(options.RSmarker,  options.testName)

x = list(allD.keys())
for num, i in enumerate(x):
    px = allD[i].split('\t')

    a1 = px[0].split(':')[0]
    a2 = px[1].split(':')[0]

    ##  geno of SNP 1

    gS1 = px[3].split(',')


    pA = int(px[0].split(':')[1]) * 1.0/ int(px[2])
    pa = int(px[1].split(':')[1]) * 1.0/ int(px[2])

    for j in x[num+1:]:
        qx  = allD[j].split('\t')

        b1 = qx[0].split(':')[0]
        b2 = qx[1].split(':')[0]

        ## geno of SNP 2
        gS2 = qx[3].split(',')
        n_p11 = 0
        n_p22 = 0
        n_p12 = 0
        n_p21 = 0


        pB  = int(qx[0].split(':')[1]) * 1.0 / int(qx[2])
        pb  = int(qx[1].split(':')[1]) * 1.0 / int(qx[2])


        for n, bg in enumerate(gS1):

            bh = gS2[n]
            hapType = [ bg[0] + bh[0], bg[1]+bh[1]]

            for haplo in hapType:

                if haplo == a1+ b1:
                    n_p11 += 1
                elif haplo ==  a2+ b2:
                    n_p22 += 1
                elif haplo ==  a1+ b2:
                    n_p12 += 1
                elif haplo ==  a2+ b1:
                    n_p21 += 1

        # http://awarnach.mathstat.dal.ca/~joeb/biol3046/PDFs/PopGen2._linkage.pdf
        # http://pbgworks.org/sites/pbgworks.org/files/measuresoflinkagedisequilibrium-111119214123-phpapp01_0.pdf

        # print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}'.format(i,j,  pA,pa, pB,pb, n_p11 *0.5/peopleN, n_p22*0.5/peopleN, n_p12*0.5/peopleN, n_p21 * 0.5/peopleN))
        D_sq = ((n_p11 *0.5/peopleN) * ( n_p22*0.5/peopleN)  -  (n_p12*0.5/peopleN) * (n_p21 * 0.5/peopleN) ) **2
        r_sq = D_sq / (pA * pa * pB * pb)

        print('{0}\t{1}\t{2}\t{3}'.format(i,j, D_sq, r_sq))
