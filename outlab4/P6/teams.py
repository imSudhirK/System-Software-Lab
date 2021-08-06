import csv
import json
import random

##6A

def makeTeams(total,each):
    try:
           total%each
    except ZeroDivisionError:
        print ("given wrong arguements")
    except ValueError:
        print ("given intervalues only")
    finally:
        if(total%each!=0):
            print ("remove %d of players" %(total%each))

##6B            
csvfile=open("newfile.csv","w")
fieldnames=['team','loyality','number']
writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
writer.writeheader()
k=random.sample(range(1,1001),100)
z1=[]
for i in range(65,91):
    for j in range(1,11):
        z1.append(chr(i))
#print k[7]
for i in range(1,101):
    z=str(random.randint(1,10))
    z2=str(k[i-1])
    z3=z1[i-1]
    writer.writerow({'team':z3,'loyality':z,'number':z2})
csvfile.close()
csv2file=open("newfile.csv","r")
jsonfile=open("file.json","w")
fieldnames=('team','loyality','number')
reader = csv.DictReader(csv2file, fieldnames)
for row in reader:
    json.dump(row,jsonfile)
   # jsonfile.write('\n')
csv2file.close()
jsonfile.close()

data=[]
csv3file=open("newfile.csv",'rU')
csvReader=csv.DictReader(csv3file)
for row in csvReader:
    data.append(row)

    
    


 
q=open("file.json",'w')
q.write(json.dumps(data,indent=4))
q.close()

r=open("file.json",'rU')
data2=json.load(r)



transfer=open('transfer.txt','rU')
lines=transfer.readlines()
ravi=[]
for line in lines:
         john=line.split()
         ravi.append(john)

count= 0

class Nosuchteam(Exception):
   pass

class Nosuchnumber(Exception):
   pass

for i in range(0,len(ravi)):
    a=0
    b=0
    try:
        min_loyality=11
        for j in range(0,100):
            if int(ravi[i][1])==int(data2[j]['number']):
                a=a+1
        for j in range(0,100):
            if (ravi[i][0])==(data2[j]['team']):
                b=b+1    
    
        for j in range(0,100):
            
            if  int(ravi[i][1])==int(data2[j]['number']):
                
                if (65<=ord(ravi[i][0])) and (ord(ravi[i][0])<75):
                    
                    for z in range(0,100):
                        if (ravi[i][0])==data2[z]['team']:
                            
                            if int(data2[z]['loyality'])<(min_loyality):
                                min_loyality=int(data2[z]['loyality'])
                                teja=z
                    
                    if (min_loyality)>7:
                        print (" no player with loyality less than 7 ")
                    elif ravi[i][0]!=data2[j]['team']:
                        print ("Transfer Complete")
                        
                        temp1=data2[j]['number']
                        temp2=data2[j]['loyality']
                        data2[j]['number']=data2[teja]['number']
                        data2[j]['loyality']=data2[teja]['loyality']
                        data2[teja]['number']=temp1
                        data2[teja]['loyality']=temp2
                        count=count+1
                        
                    else:
                        count=count+0
        if (a==0):
            raise Nosuchnumber
        if (b==0):
            raise Nosuchteam
    except  Nosuchteam:
        print ("Try another transfer(Wrong team name")
    except  Nosuchnumber:
        print ("Try another transfer(Wrong player number)")
   
                
print (count)


s=open("players.json",'w')
s.write(json.dumps(data2,indent=4))
s.close()
r.close







                                          
                                      
                              
                              
                  

