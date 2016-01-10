__author__ = 'ysun138'
import codecs

# rfile1 = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Conference_instance_coordinates.csv",'r',"utf-8")
# rfile2 = codecs.open("location_for_conference_set.txt",'r',"utf-8")

rfile1 = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Affiliations_coordinates.csv",'r',"utf-8")
rfile2 = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Affiliations_locations.txt",'r',"utf-8")

set1 = set()
set2 = set()

for line in rfile1:
    l = line.split("\t")
    name = l[0]
    set1.add(name)
print set1.__len__()
rfile1.close()

for line in rfile2:
    line = line.rstrip()
    set2.add(line)


wfile1 = codecs.open("missing_location.csv","w","utf-8")
wfile2 = codecs.open("finding_location.csv",'w',"utf-8")
for element in set2:
    if(set1.__contains__(element)== False):
        wfile1.write(element+"\n")
    else:
        wfile2.write(element+"\n")
wfile1.close()
wfile2.close()


for element in set2:
    set1.discard(element)
print set1
print set1.__len__()

wfile = codecs.open("writing_test.csv",'w',"utf-8")
for element in set1:
    wfile.write(element+"\n")
