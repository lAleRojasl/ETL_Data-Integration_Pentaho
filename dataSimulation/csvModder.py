import csv
import string
import random
from random import randint
from datetime import date, timedelta
import operator
import numpy as np


csvData = []

#Cargamos los datos a modificar
with open('LineasXOrden.csv', 'r') as dataReadCSV:
    reader = csv.reader(dataReadCSV)
    csvData = list(reader)
    dataReadCSV.close()

#Guardamos datos modificados
with open('LineasXOrdenMod.csv', 'w', newline='') as dataWriterCSV:    
    dataWriter = csv.writer(dataWriterCSV, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    for row in csvData:
        if(csvData.index(row) == 0):
            dataWriter.writerow(row)
            continue
        row[1] = int(row[1])+ 1
        dataWriter.writerow(row)


print("Done")
