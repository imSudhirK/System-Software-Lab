#! /usr/bin/python3

import sys 
import csv
import numpy as np 

try: 
   csvReader = open ("info_day.csv" ,"rU")
   dayHandle = csv.reader(csvReader)
except IOError: 
   print("File not found or path is incorrect")
finally:
   cTemp=np.array([] , dtype=np.float)
   Humidity=np.array([] , dtype=np.float)
   Light=np.array([] , dtype=np.float)
   CO2=np.array([] , dtype=np.float)
   next(dayHandle)
   for line in dayHandle:     
        cTemp = np.append(cTemp , np.array(float (line[1])))
        Humidity = np.append(Humidity , np.array(float (line[2])))
        Light = np.append(Light , np.array(float (line[3])))
        CO2 = np.append(CO2 , np.array( float (line[4]))) 
   fTemp = (9.0/5.0)*cTemp +32   
  
csvfile = open ("transformed.csv" ,  "w+")
fieldnames = ["Day","Temperature","Humidity","Light","CO2"]
writer = csv.DictWriter(csvfile , fieldnames= fieldnames)
writer.writeheader()
writer.writerow({ "Day": "Monday"   , "Temperature": fTemp[0] ,"Humidity": Humidity[0] ,"Light": Light[0]   ,"CO2": CO2[0]})
writer.writerow({ "Day": "Tuesday"  , "Temperature": fTemp[1] ,"Humidity": Humidity[1] ,"Light": Light[1]   ,"CO2": CO2[1]})
writer.writerow({ "Day": "Wednesday", "Temperature": fTemp[2] ,"Humidity": Humidity[2] ,"Light": Light[2]   ,"CO2": CO2[2]})
writer.writerow({ "Day": "Thursday" , "Temperature": fTemp[3] ,"Humidity": Humidity[3] ,"Light": Light[3]   ,"CO2": CO2[3]})
writer.writerow({ "Day": "Friday"   , "Temperature": fTemp[4] ,"Humidity": Humidity[4] ,"Light": Light[4]   ,"CO2": CO2[4]})
writer.writerow({ "Day": "Saturday" , "Temperature": fTemp[5] ,"Humidity": Humidity[5] ,"Light": Light[5]   ,"CO2": CO2[5]})
writer.writerow({ "Day": "Sunday"   , "Temperature": fTemp[6] ,"Humidity": Humidity[6] ,"Light": Light[6]   ,"CO2": CO2[6]})
csvfile.close()
   


















