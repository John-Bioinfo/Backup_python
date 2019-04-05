#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import defaultdict
import numpy as np
import sys
import os

#denoisedFile = '../1810831.denoisedCR.tsv'
#segFile      = 'segfiles/1810831.modelFinal.seg'
denoisedFile = sys.argv[1]
dfile        = os.path.basename(denoisedFile).split('.')[0]
segFile      = 'segfiles/' + dfile + '.modelFinal.seg'

Ls = []

xs = open( segFile, 'r' )
for x in xs:
    if not (x.startswith('@') or x.startswith('CONTIG')):
        a = x.rstrip().split('\t')
        Ls.append('\t'.join(a[:3]))
xs.close()

dict_of_segments  = defaultdict(list)
seg_index = 0
xd = open( denoisedFile, 'r' )
for x in xd:
    if not (x.startswith('@') or x.startswith('CONTIG')):
        b = x.rstrip().split('\t')
        b_start = int(b[1])
        b_end   = int(b[2])

        b_pos   = (b_start + b_end) / 2
        for num,i in enumerate(Ls[seg_index:]):
            s = i.split('\t')
            if b[0] == s[0] and b_pos > int(s[1]) and b_pos < int(s[2]):
                #dict_of_segments[i].append('\t'.join(b[:3]))
                dict_of_segments[i].append( 2 ** abs(float(b[3])))
                seg_index = num + seg_index
                break

xd.close()

_highS = []
total_interval = 0
for i in dict_of_segments:
    a = np.array(dict_of_segments[i])
    
    if len(a) > 1:
        mean_a = np.mean(a)
        std_a  = np.std(a, ddof=1, axis=0)
    else:
        mean_a = a[0]
        std_a  = 0.0

    cv_a   = std_a / mean_a
    #print('{0:.3f}\t{1:.3f}\t{2:.3f}\t{3}'.format(mean_a, std_a, cv_a, i))

    _highS.append(mean_a)

    total_interval += len(dict_of_segments[i])
#print(total_interval)
mean_std = np.mean(np.array(_highS))

new_S = []
for i in _highS:
    if i <= mean_std * 4:
        new_S.append(i)

abnormal_Std = []
for i in new_S:
    if i - mean_std > mean_std * 0.1:
        abnormal_Std.append(i)

print('{0:.2f}'.format(100.0 * len(abnormal_Std) / len(new_S)))




