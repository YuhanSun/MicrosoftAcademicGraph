__author__ = 'ysun138'

rfile = open("D:\MicrosoftAcademicGraph_2015_11\ConferenceInstances.txt")
wfile = open("D:\MicrosoftAcademicGraph_2015_11\ConferenceInstances_location.txt",'w')

location_set = set()

for line in rfile:
    l = line.split("\t")
    location = l[4]
    location_set.add(location)

print location_set.__len__()

for element in location_set:
    wfile.write(element+"\n")

rfile.close()
wfile.close()
