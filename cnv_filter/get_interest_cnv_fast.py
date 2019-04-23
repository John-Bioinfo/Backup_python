#!/usr/bin/env python
# -*- coding: UTF-8 -*-

bedF = "BGI_pt2.bed"

d_region = []

bedHandle = open(bedF, "r")
for line in bedHandle:
    a = line.strip().split("\t")
    r = "\t".join(a[0:3])
    d_region.append(r)
bedHandle.close()

CNV_data = "WBC.cnv.xls"

opCNV = open(CNV_data, "r")
outName = CNV_data.strip(".xls") + "_results.xls"

region_index = 0

out = open(outName, "w")
for line in opCNV:
    if line.startswith("CNV_type"):
        continue
    else:
        z = line.strip().split("\t")
        chrA = z[1]
        chrName = chrA.split(":")[0]
        rs = chrA.split(":")[1].split("-")
 
        siteS = int(rs[0])
        siteE = int(rs[1])

        first_r = d_region[region_index:][0]
        fc      = first_r.split('\t')
        bed_chrNum = fc[0].replace('chr', '')

        if bed_chrNum == 'X':
            bed_chrNum = 24
        elif bed_chrNum == 'Y':
            bed_chrNum = 25
        elif bed_chrNum == 'M':
            bed_chrNum = 26
        else:
            bed_chrNum = int(bed_chrNum)
        if (chrName == fc[0] and siteE < int(fc[1])) or (chrName not in ['chrX', 'chrY', 'chrM'] and bed_chrNum > int(chrName.replace('chr', ''))):
            continue
        
        for num,i in enumerate(d_region[region_index:]):
            cx = i.split("\t")
            c = cx[0]
            start = int(cx[1])
            end   = int(cx[2])
            
            if chrName ==c and ((siteS >= start and siteS <= end) or (siteE >= start and siteE <= end)):
                out.write(line)
                region_index = num + region_index
                break
out.close()
opCNV.close() 





