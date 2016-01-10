__author__ = 'ysun138'
import codecs

location_set = set()
original_input = codecs.open("D:\MicrosoftAcademicGraph_2015_11\Conference_instance_coordinates.csv",'r',"utf-8")
for line in original_input:
    location_set.add(line.split("\t")[0])
original_input.close()

inputfile = codecs.open("MapQuest_conference.gpx",'r',"utf-8")
outfile = codecs.open("temp.gpx","a","utf-8")

inputfile.readline()
inputfile.readline()

while(True):
    line = inputfile.readline()
    if(line.__contains__("</gpx>")):
        break
    if(line.__contains__("<wpt lat=\"39.78373\" lon=\"-100.445882\">")):
        inputfile.readline()
        inputfile.readline()
        inputfile.readline()
        continue
    else:
        outfile.write(line)
        outfile.write(inputfile.readline())
        outfile.write(inputfile.readline())
        outfile.write(inputfile.readline())

inputfile.close()
outfile.close()