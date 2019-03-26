#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import time
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Align.Applications import MuscleCommandline

muscle = "/data2/test/zyqiao_test/RNAseq_data/PEAR/muscle3.8.31_i86linux64"
work_dir = "/data2/test/zyqiao_test/htslib_test/HLA_fasta/"

def P_F(f2):
    f_h = open(f2, 'r')
    seqs_Dict = {}
    for Line in f_h:
        if Line[0]==">":
            Name=Line.strip()[1:]
            seqs_Dict[Name] = ""
        else:
            try:
                #try to append with +=
                #assumes Name is a key
                seqs_Dict[Name]+=Line.strip()
            except KeyError:
                seqs_Dict[Name]=Line.strip()
            except UnboundLocalError:
                continue
    f_h.close()
    return seqs_Dict

def AlignStrs(str1, str2):
    sc = ""
    for num, c in enumerate(str1):
        if c == str2[num]:
            sc+=c
        else:
            sc+="-"
    rsc = sc[::-1]
    for n, i in enumerate(sc):
        if i != "-":
            tn = n
            break

    for m, j in enumerate(rsc):
        if j != "-":
            tm = m
            break
    slen = len(sc)

    outAlignC = ""
    for num, i in enumerate(sc):
        if num < n or num > slen - m -1:
        #print ("-", end ="")
            outAlignC += "-"
        elif sc[num] == str1[num]:
        #print (i,   end ="")
            outAlignC += i
        else:
        #print ("*", end ="")
            outAlignC += "*"

    return outAlignC

def alignSEQ( seqfile, geneName):

    fname = os.path.basename(seqfile)
    outName =  "TMP_geneName_{0}".format(fname)
    m_cline = MuscleCommandline(muscle, input = seqfile, out = work_dir +'/'+ outName, clw=False)
    m_cline()

    AllSeqs = P_F(outName)
    s = list(AllSeqs.keys())
    
    seqLength = len(AllSeqs[s[0]])
    s1 = AllSeqs[s[0]]
    s2 = AllSeqs[s[1]]    

    print('{0} {1}'.format(s[0], s[1]))
    return s1, s2, seqLength

os.chdir(work_dir)
#sa, sb, sl = alignSEQ('/data2/test/lohhla_test/Test_620V2/1910008_hlas/types_B.fa', 'HLA-B')
sa, sb, sl = alignSEQ(sys.argv[1], 'HLA-B')

PL = []
for num,s in enumerate(sa):
    base_b = sb[num]
    if base_b != s :
        #print("{0}\t{1}\t{2}".format(num, s, base_b ))
        PL.append(num)

nodes =  [ 0 ]
for i in range(1,len(PL)):
    if PL[i] - PL[i-1] > 15:
        nodes.append(i)

nodes.append(len(PL))
for i in range(len(nodes)-1):
    block_start = nodes[i]
    block_end   = nodes[i+1]
    full_pos = PL[block_start:block_end]

    a_pos = []
    b_pos = []

    for j in full_pos:
        a_pos.append(j  - sa[:j+1].count('-'))
        b_pos.append(j  - sb[:j+1].count('-'))

    print('{0}'.format(','.join([str(i) for i in a_pos])), end=' ')

    print('{0}'.format(','.join([str(i) for i in b_pos])))

