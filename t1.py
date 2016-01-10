__author__ = 'ysun138'

file1 = open("D:\Graph_05_13\graph_2015_1_24_mfc\data\Real_Data\uniprotenc_150m\Random_spatial_distributed\\20\entity.txt")
file2 = open("D:\Graph_05_13\graph_2015_1_24_mfc\data\Real_Data\uniprotenc_150m\Random_spatial_distributed\\20\\new_entity.txt")
i = 0
max = 100000
l1 = []
l2 = []
for line in file1:
    i+=1
    l1.append(line)
    if(i == max):
        break

i = 0
for line in file2:
    i+=1
    l2.append(line)
    if(i == max):
        break

for i in range(0, l1.__len__()):
    if(str(l1[i]).__eq__(str(l2[i]))):
        continue
    else:
        print i