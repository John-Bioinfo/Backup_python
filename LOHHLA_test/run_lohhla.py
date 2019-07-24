#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from glob import glob
import argparse
import subprocess
import sys
import os

# get HLA fasta

def extract_fas(in_typing_res, fa_dir):
    file_dir = os.path.dirname(in_typing_res)
    os.chdir(file_dir)
    sampleID = os.path.basename(in_typing_res).split('_')[0]

    if not os.path.exists(sampleID + '_hlas'):
        os.mkdir(sampleID + '_hlas')

    fh = open( os.path.basename(in_typing_res), 'r' )
    for line in fh:
        for hla_t in ['A', 'B', 'C']:
            types=[]
            if line.startswith('HLA-'  + hla_t):
                x = line.strip().split('\t')
                types.extend(x[1:])
                hlasOut =open(sampleID + '_hlas/hlas_' + hla_t , 'w' )
                hlaFa   = open(sampleID + '_hlas/types_'  + hla_t  + '.fa' , 'w')
                for i in types:
                    testFile = fa_dir + i + '.fasta'
                    if os.path.exists(testFile):
                        faCon = open(testFile, 'r').read()
                        hlaFa.write(faCon.lower())
                        hlasOut.write(i + '\n')
                hlasOut.close()
                hlaFa.close()
    fh.close()
    os.chdir("../")
    return sampleID + '_hlas'

def pick_norm(files, hlas_dir):
    sampleI = hlas_dir.split('_')[0]
    for i in files:
        if i == sampleI + '_normal_sorted.bam':
            return i
            break 

def create_sampleList(bam_dirs, hlas_dir, HLA_D):
    for i in bam_dirs:
        all_files = os.listdir(i)
        normf = pick_norm(all_files, hlas_dir)
        if normf != None: 
            return (i, normf, HLA_D + '/' +hlas_dir)
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s' ,'--solution_f', default="solutions", help='solution_dir')

    parser.add_argument('-d' , '--hla_dir', help='hla_fas_dir')
    parser.add_argument('-a' , '--all_hla_fas', default= '/data2/test/lohhla_test/hla_seq_complete/', help='hla_fas_dir')

    args = parser.parse_args()

## check solution dir and hla fasta dir

if not os.path.exists(args.solution_f):
    sys.exit("The solution file does not exist, please check it.")

if not os.path.exists(args.all_hla_fas):
    sys.exit("The HLA full fasta dir does not exist, please check.")


#  get ALL HLA Fas

hlas_dirs = []

hla_types = glob( args.hla_dir + "/*_hla.txt")

for i in hla_types:
    hlas_dirs.append( extract_fas(i, args.all_hla_fas) )
    print(i)
    #hlas_dirs.append(   "/data2/test/lohhla_test/hla_seq_complete/"

## generate shells

curr_dir = os.path.abspath('.') + '/' 
outList = open('test_samples.txt', 'w')

outList.write('sample\toutdir\tnormalbam\tbamdir\thlapath\thla_type\n')
bams = glob("Sample_*_bam")
for ht in ['H__A', 'H__B', 'H__C']:
    for i in hlas_dirs:
        bamdir, norm_bam, hlas_d = create_sampleList(bams, i, args.hla_dir)
        sample_id = bamdir.split('_')[1]
        abs_hlaD = os.path.abspath(hlas_d)
        outList.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(sample_id, curr_dir + 'LOH_' + sample_id + '/', 
curr_dir+bamdir + '/'+norm_bam, curr_dir + bamdir +'/', abs_hlaD, ht))

outList.close()
subprocess.call('Rscript ../generate_LOHTestt.R test_samples.txt ' + curr_dir+'solutions/', shell=True)


## run all samples

subprocess.call('sh test_lohhla.sh', shell=True)


