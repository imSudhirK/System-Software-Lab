import csv
import json
r = open("infinity_stones.json",'rU')
data=json.load(r)
outputfile=open("update.json","w")

for i in range(0,6):
     data["Infinity Stones"][i]['Containment Unit']="Infinity Gautlet"
outputfile.write(json.dumps(data,indent=4))
r.close
outputfile.close

