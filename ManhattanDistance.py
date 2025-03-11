# Manhattan Distance
import os
import glob

def Manhattan(file1, file2):
    dic = {}
    MHD = 0
    file1 = open(file1,"r")
    file2 = open(file2,"r")
    for line in file1:
        line = line.strip("\n")
        name, pro = line.split("\t")
        dic[name] = float(pro)

    for line in file2:
        line = line.strip("\n")
        name, pro = line.split("\t")
        pro = float(pro)
        if name in dic:
            d = abs(pro - dic[name])
            MHD += d
    return MHD


file_list = glob.glob("*.tsv")
for i in range(len(file_list)):
    for j in range (i+1, len(file_list)):
        file1, file2 = file_list[i], file_list[j]
        print(file1, file2, Manhattan(file1,file2))
