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
   dTemp=np.array([] , dtype=np.float)
   dHumidity=np.array([] , dtype=np.float)
   dLight=np.array([] , dtype=np.float)
   dCO2=np.array([] , dtype=np.float)
   next(dayHandle)
   for dline in dayHandle:     
        dTemp = np.append(dTemp , np.array(float (dline[1])))
        dHumidity = np.append(dHumidity , np.array(float (dline[2])))
        dLight = np.append(dLight , np.array(float (dline[3])))
        dCO2 = np.append(dCO2 , np.array( float (dline[4])))

try: 
       csvReader1 = open ("info_night.csv" ,"rU")
       nightHandle = csv.reader(csvReader1)
except IOError: 
       print("File not found or path is incorrect")
finally:
       nTemp=np.array([] , dtype=np.float)
       nHumidity=np.array([] , dtype=np.float)
       nLight=np.array([] , dtype=np.float)
       nCO2=np.array([] , dtype=np.float)
       next(nightHandle)
       for nline in nightHandle:     
           nTemp = np.append(nTemp , np.array(float (nline[1])))
           nHumidity = np.append(nHumidity , np.array(float (nline[2])))
           nLight = np.append(nLight , np.array(float (nline[3])))
           nCO2 = np.append(nCO2 , np.array( float (nline[4]))) 

csvfile = open ("​info_combine.csv" ,  "w+")
fieldnames = ['Day'  , 'Temperature(Day)' ,'Temperature(Night)','Humidity(Day)' , 'Humidity(Night)','Light(Day)', 'Light(Night)','CO2(Day)','CO2(Night)']
writer = csv.DictWriter(csvfile , fieldnames= fieldnames)
writer.writeheader()
writer.writerow({ 'Day':'Monday'   , 'Temperature(Day)': dTemp[0] , 'Temperature(Night)': nTemp[0] ,'Humidity(Day)': dHumidity[0],'Humidity(Night)': nHumidity[0], 'Light(Day)':dLight[0] , 'Light(Night)': nLight[0],'CO2(Day)': dCO2[0], 'CO2(Night)': nCO2[0] })
writer.writerow({ 'Day':'Tuesday'  , 'Temperature(Day)': dTemp[1] , 'Temperature(Night)': nTemp[1] ,'Humidity(Day)': dHumidity[1],'Humidity(Night)': nHumidity[1], 'Light(Day)':dLight[1] , 'Light(Night)': nLight[1],'CO2(Day)': dCO2[1], 'CO2(Night)': nCO2[1] })
writer.writerow({ 'Day':'Wednesday', 'Temperature(Day)': dTemp[2] , 'Temperature(Night)': nTemp[2] ,'Humidity(Day)': dHumidity[2],'Humidity(Night)': nHumidity[2], 'Light(Day)':dLight[2] , 'Light(Night)': nLight[2],'CO2(Day)': dCO2[2], 'CO2(Night)': nCO2[2] })
writer.writerow({ 'Day':'Thursday' , 'Temperature(Day)': dTemp[3] , 'Temperature(Night)': nTemp[3] ,'Humidity(Day)': dHumidity[3],'Humidity(Night)': nHumidity[3], 'Light(Day)':dLight[3] , 'Light(Night)': nLight[3],'CO2(Day)': dCO2[3], 'CO2(Night)': nCO2[3] })
writer.writerow({ 'Day':'Friday'   , 'Temperature(Day)': dTemp[4] , 'Temperature(Night)': nTemp[4] ,'Humidity(Day)': dHumidity[4],'Humidity(Night)': nHumidity[4], 'Light(Day)':dLight[4] , 'Light(Night)': nLight[4],'CO2(Day)': dCO2[4], 'CO2(Night)': nCO2[4] })
writer.writerow({ 'Day':'Saturday' , 'Temperature(Day)': dTemp[5] , 'Temperature(Night)': nTemp[5] ,'Humidity(Day)': dHumidity[5],'Humidity(Night)': nHumidity[5], 'Light(Day)':dLight[5] , 'Light(Night)': nLight[5],'CO2(Day)': dCO2[5], 'CO2(Night)': nCO2[5] })
writer.writerow({ 'Day':'Sunday'   , 'Temperature(Day)': dTemp[6] , 'Temperature(Night)': nTemp[6] ,'Humidity(Day)': dHumidity[6],'Humidity(Night)': nHumidity[6], 'Light(Day)':dLight[6] , 'Light(Night)': nLight[6],'CO2(Day)': dCO2[6], 'CO2(Night)': nCO2[6] })   
csvfile.close()
   



















