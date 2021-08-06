import json
import csv
file=open("infinity_stones.json",'rU')
data=json.load(file)
print(data)
outputfile=open("infinity_stones.csv","w")
outputWriter=csv.writer(outputfile)
count = 0
for each in data["Infinity Stones"]:
    if count==0:
        header = each.keys() 
        outputWriter.writerow(header)
        count=count+1
    outputWriter.writerow(each.values())
file.close()
    
        
