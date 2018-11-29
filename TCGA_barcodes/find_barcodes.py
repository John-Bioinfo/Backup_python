#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys


if len(sys.argv) < 3:
    sys.exit("please provide pos file and maf file!")
posfile = sys.argv[1]
maffile = sys.argv[2]

dP = {}

handle_P = open(posfile, "r")
for line in handle_P:
    px = line.strip().split("\t")
    dP["chr" + px[1] + ":" + px[2]] = 1

handle_P.close()    

fh = open(maffile, "r")
for line in fh:
    if line.startswith("#") or line.startswith("Hugo_Symbol"):
        continue
    else:
        x = line.strip().split("\t")
        start = int(x[5])
        end   = int(x[6])

        for i in range(start, end + 1):
            
            p = x[4]+":" + str(i)
            if p in dP:
                print("{0}\t{1}".format(x[15], x[16]))

fh.close()



