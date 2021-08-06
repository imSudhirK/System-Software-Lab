#! /usr/bin/python3

import sys 
import statistics
import csv
import numpy as np 
from statistics import stdev

try: 
   csvReader = open ("info_day.csv" ,"rU")
   dayHandle = csv.reader(csvReader)
except IOError: 
   print("File not found or path is incorrect")
finally:
   Temp=np.array([] , dtype=np.float)
   Humidity=np.array([] , dtype=np.float)
   Light=np.array([] , dtype=np.float)
   CO2=np.array([] , dtype=np.float)
   next(dayHandle)
   for line in dayHandle:     
        Temp = np.append(Temp , np.array(float (line[1])))
        Humidity = np.append(Humidity , np.array(float (line[2])))
        Light = np.append(Light , np.array(float (line[3])))
        CO2 = np.append(CO2 , np.array( float (line[4])))      
   meanTemp = statistics.mean(Temp)
   meanHumidity =  statistics.mean(Humidity)
   meanLight = statistics.mean(Light)
   meanCO2 =  statistics.mean(CO2) 
   stdDevTemp = statistics.stdev(Temp)
   stdDevHumidity = statistics.stdev(Humidity)
   stdDevLight =   statistics.stdev(Light)
   stdDevCO2 =  statistics.stdev(CO2) 

csvfile = open ("new.csv" ,  "w+")
fieldnames = ['Field'  , 'Mean' , 'std.Dev']
writer = csv.DictWriter(csvfile , fieldnames= fieldnames)
writer.writeheader()
writer.writerow({ 'Field': "Temperature" , 'Mean': meanTemp ,'std.Dev': stdDevTemp })
writer.writerow({ 'Field': "Humidity" , 'Mean': meanHumidity ,'std.Dev': stdDevHumidity })
writer.writerow({ 'Field': "Light" , 'Mean': meanLight ,'std.Dev': stdDevLight })
writer.writerow({ 'Field': "CO2" , 'Mean': meanCO2 ,'std.Dev': stdDevCO2 })
csvfile.close()
try:
    csvReader2= open ("new.csv" , "rU")
    csvHandle =csv.reader(csvReader2)
except IOError:
    print ("file not found")
finally:
    for line in csvHandle:
               print(line)




















