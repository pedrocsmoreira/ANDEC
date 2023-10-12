import csv
import numpy

arr = numpy.zeros((68, 2))

with open('ANDEC.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for i,row in enumerate(reader):
        x = row[2].split('/')
        arr[i, 0] = x[-1]
        arr[i, 1] = row[3].replace('"', '')



