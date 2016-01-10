__author__ = 'ysun138'
import codecs

inputfile = codecs.open("D:\MicrosoftAcademicGraph_2015_11\ConferenceInstances_location.gpx",'r',"utf-8")
outfile = codecs.open("D:\MicrosoftAcademicGraph_2015_11\CConferenceInstances_coordinate.csv","w","utf-8")

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
    # print lat,lon
    line = inputfile.readline()
    line = line.rstrip()
    l = line.split("<name>")
    l = l[1].split("</name>")
    location_name = l[0]
    # print location_name
    if(location_set.__contains__(location_name) == False):
        location_set.add(location_name)
        outfile.write(location_name+"\t"+lat+"\t"+lon+"\n")

    inputfile.readline()
    inputfile.readline()


inputfile.close()
outfile.close()

