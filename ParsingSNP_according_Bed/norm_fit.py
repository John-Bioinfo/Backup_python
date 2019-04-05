#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from glob import glob
from scipy.stats import norm
import numpy as np
import sys
import os


def cacSTD(denoisedFile, s):

    Ls = []

    xd = open( denoisedFile, 'r' )
    for x in xd:
        if not (x.startswith('@') or x.startswith('CONTIG')):
            b = x.rstrip().split('\t')
            #if abs(float(b[3])) < 1.16:
            if 2 ** abs(float(b[4])) < s:
                #Ls.append( 2 ** float(b[3]))
                Ls.append( 2 ** float(b[4]))

    xd.close()

    a = np.array(Ls)
    std_a  = np.std(a, ddof=1, axis=0)
    #print('{0:.3f}\t{1:.3f}\t{2:.3f}\t{3}'.format(mean_a, std_a, cv_a, i))

    return std_a

_highS = []
pngs = glob('./normal/*.png')
for i in pngs:
    filelabel = os.path.basename(i).split('.')[0]
    #defile = '../' + filelabel +'.denoisedCR.tsv' 
    defile = '../' + filelabel +'.cr.seg' 
    sk = cacSTD(defile, 5.5)
    _highS.append(sk)

res_S = []
for i in glob('abnormal/*.png'):
    print(i)
    #defile = '../' + os.path.basename(i).split('.')[0] +'.denoisedCR.tsv'
    defile = '../' + os.path.basename(i).split('.')[0] +'.cr.seg'
    res_S.append(cacSTD(defile, 60))

mu, std = norm.fit(_highS)
print(mu)
print(std)
for i in res_S:
    c       = norm.cdf(i, loc=mu, scale=std)
    print( 1 -  c  )
