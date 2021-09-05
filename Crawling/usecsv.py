import csv, os, re

def opencsv(filename):
    f = open(filename, 'r')
    csvreader = csv.reader(f)
    output = []
    for i in csvreader:
        output.append(i)
    f.close()
    return output

def writecsv(filename, input_list):
    with open(filename, 'w', newline='') as f:
        csvwriter = csv.writer(f, delimiter = ',')
        csvwriter.writerows(input_list)

def switch(list_name):
    for i in list_name:
        for j in i:
            try : list_name[list_name.index(i)][i.index(j)] = int(re.sub(',', '', j))
            except : continue
    return list_name
