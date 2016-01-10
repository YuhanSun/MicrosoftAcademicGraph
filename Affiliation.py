__author__ = 'ysun138'
import codecs

'''
rfile = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Affiliations.txt",'r',"utf-8")
location_set = set()
for line in rfile:
    line = line.rstrip()
    l = line.split("\t")
    location_set.add(l[1])
rfile.close()
print location_set.__len__()

wfile = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Affiliations_location.txt",'w',"utf-8")
for element in location_set:
    wfile.write(element+"\n")
wfile.close()
'''

inputfile = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Affiliations_coordinate.gpx",'r',"utf-8")
outfile = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Affiliations_coordinate.csv","w","utf-8")

inputfile.readline()
inputfile.readline()

location_set = set()

while(True):
    line = inputfile.readline()
    if(line.__contains__("</gpx>")):
        break
    l = line.split("\"")
    lat = l[1]
    lon = l[3]
    print lat,lon
    line = inputfile.readline()
    line = line.rstrip()
    l = line.split("<name>")
    l = l[1].split("</name>")
    location_name = l[0]
    if(location_set.__contains__(location_name) == False):
        location_set.add(location_name)
        outfile.write(location_name+"\t"+lat+"\t"+lon+"\n")

    inputfile.readline()
    inputfile.readline()


inputfile.close()
outfile.close()
