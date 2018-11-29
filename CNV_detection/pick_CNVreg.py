



#a = open("CNV_ALL.target.dep", "r")
a = open("CopyNumber_New.xls", "r")

for line in a:
    z = line.strip().split("\t")
    #t01 = int(z[6]) 
    t01 = int(z[4]) 

    #tnorm = int(z[7])
    tnorm = int(z[5])

    try:
        x = 1.0* t01/tnorm 
        if x > 1.4:
            print(line.strip())
        elif x < 0.8:
            print(line.strip())
    except ZeroDivisionError:
        #print("Depth0" + line.strip())
        pass
a.close()





