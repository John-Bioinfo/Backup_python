#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from collections import defaultdict
import os, sys
import argparse

def data_process(alignDep1, alignDep2, window_size, step, out_f, bed_f = "target_region.bed"):
    Dep1_handle = open(alignDep1, 'r')      # 
    chromo1 = defaultdict(dict)

    for i in Dep1_handle:
        if i.startswith("Chr"):
            continue
        else:
            splits = i.rstrip().split("\t")
            chr_name = splits[0]
            Position = int(splits[1]) + int(splits[6])
            steps_in_win = int(window_size/step)
            chr_win_start = (int(Position//step) - steps_in_win +1) * step
            depth1    = int(splits[7])
            #print (Position, steps_in_win, chr_win_start)
            for win in range(chr_win_start, chr_win_start + window_size, step):
                if win >= 0 and win in chromo1[chr_name]:
                    chromo1[chr_name][win] += depth1
                elif win >= 0:
                    chromo1[chr_name][win] = depth1
    Dep1_handle.close()

    Dep2_handle = open(alignDep2, 'r')      # 
    chromo2 = defaultdict(dict)

    for i in Dep2_handle:
        if i.startswith("Chr"):
            continue
        else:
            splits = i.rstrip().split("\t")
            chr_name = splits[0]
            Position = int(splits[1]) + int(splits[6])
            steps_in_win = int(window_size/step)
            chr_win_start = (int(Position//step) - steps_in_win +1) * step
            depth2    =  int(splits[7])
            for win in range(chr_win_start, chr_win_start + window_size, step):
                if win >= 0 and win in chromo2[chr_name]:
                    chromo2[chr_name][win] += depth2
                elif win >= 0:
                    chromo2[chr_name][win] = depth2
    Dep2_handle.close()

    AllChr = set()

    for i in chromo1:
        AllChr.add(i)
    for i in chromo2:
        AllChr.add(i)

    sf = list(filter(lambda t: not t.lstrip("chr").isdigit(), AllChr))

    SortChr = sorted([i for i in AllChr if i not in sf], key = lambda t: int(t.lstrip("chr"))) 

    SortChr.extend(sf)
    #SortR   = sorted(AllRegion)
    DR = dict()
    a = open(bed_f, "r")

    for line in a:
        aR = line.strip().split("\t")
        reg = aR[0]+":"+aR[1] + "-" + aR[2]
        DR[reg] = 1

    a.close()
    writeF = open(out_f, "w")
    
    for c in SortChr:
        for j in chromo1[c]:
            for d in DR:
                reg_chr  = d.split(":")[0]
                reg_poss = d.split(":")[1].split("-")
                start = int(reg_poss[0])
                end   = int(reg_poss[1])

                if c == reg_chr and j >= start and j <= end and j in chromo2[c]:
                    try :
                        ratio = chromo1[c][j] * 1.0 / chromo2[c][j]
                        writeF.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6:.4f}\n".format(c, start, end, j, chromo1[c][j], chromo2[c][j], ratio))
                    except:
                        writeF.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(c, start, end, j, chromo1[c][j], 0, "--"))

                elif c == reg_chr and j >= start and j <= end and j not in chromo2[c]:
                    writeF.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n".format(c, start, end, j, chromo1[c][j], 0, "--"))

    writeF.close()
    return out_f


if __name__ == "__main__":

    USAGE = "python %s.py -i SNP_filter_result"%("Plot_Ch.py")
    parser = argparse.ArgumentParser(description = USAGE)
    parser.add_argument("-i", "--input", action = "store", required = True, help = "the depth file of tumor chr, pos and depth")
    parser.add_argument("-c", "--compareC", action = "store", help = "the filename containing normal coverage of chromosomes")
    parser.add_argument("-w", "--WS", type = int, default = 10, help = "the window size of region")
    parser.add_argument("-s", "--Step", type = int , default = 10,  help = "the step ")
    parser.add_argument("-rd", "--Targeted_bed",  default = "target_region.bed",  help = "the bedfile of Region")
    parser.add_argument("-o", "--output", action = "store", default = "CopyNumber_New.xls", help = "the Output file")

    args = parser.parse_args()
    Win_S = args.WS
    Arg_Step = args.Step
    
    if not os.path.exists(args.Targeted_bed):
        print ("""the bed file for chromosome does not exist. please provide this file. It should seem like this:  
          chr1       29679	31905
          chr2       329680	429684
          chr3       19681	29684
""")
        sys.exit("Process aborted abnormally.")
    # invoke functions to process data
    data_process(args.input, args.compareC, args.WS, args.Step, args.output, args.Targeted_bed)




