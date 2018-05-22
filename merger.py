"""
Simple, brute, Python script to merge .CSV files into one. It has been used
to merge data collected from sensors into a single file, ready to be uploaded.
Written by Alessio Torraco 2018
"""
import csv

filelist = ['temp.csv', 'barom.csv', 'smoke.csv', 'locat.csv']
headers = ['location', 'Temperature', 'Humidity', 'Pressure', 'Smoke']
temperature = []
humidity = []
pressure = []
smoke = []
location = []
result = []
t = []
h = []
p = []
s = []
min = 1000;

#read files and extract column
for fl in filelist:
    reader = csv.reader(open(fl, 'r'), delimiter=',', lineterminator='\n')
    for row in reader:
        if(fl == 'temp.csv'):
            temperature.append(row[0:1])
            humidity.append(row[1:2])
        if(fl == 'barom.csv'):
            pressure.append(row[0:1])
        if(fl == 'smoke.csv'):
            smoke.append(row[0:1])
        if(fl == 'locat.csv'):
            latitude = row[0]
            longitude = row[1]
            google = latitude +','+ longitude
            location.append(google)

writer = csv.writer ( open ( 'datalog.csv', 'w' ),delimiter=',', lineterminator='\n' )

#write header output file
writer.writerow (headers)

#conversion to list
for x in temperature:
    for key in x:
        t.append(key[0:10])
for x in humidity:
    for key in x:
        h.append(key[0:10])
for x in pressure:
    for key in x:
        p.append(key[0:10])
for x in smoke:
    for key in x:
        s.append(key[0:10])

for x in range(0, 5):
    if len(t) < min:
        min = len(t)
    if len(h) < min:
        min = len(h)
    if len(p) < min:
        min = len(p)
    if len(s) < min:
        min = len(s)
    if len(location) < min:
        min = len(location)

for x in range(0, min):
    row = [location[x], t[x], h[x], p[x], s[x]]
    writer.writerow (row)