#! /usr/bin/env python
class snake:
	def __init__ (self,name,length,venom):
	    self.name=name
	    self.length=length
	    self.venom=venom


f=open("snake.txt",'rU')
lines=f.readlines()
ravi = []
#teja = []
for line in lines:
    words = line.split()
    ravi.append(words)
z=len(ravi)
		
#    ravi.append(words)
k=ravi[0][0]
#print(k+1)
for i in range(1,int(k)+1):
    ravi[i][0] = snake(ravi[i][0],int(ravi[i][1]),int(ravi[i][2]))
#print (ravi[1][0].name)
for i in range (int(k)+2,z):
	#print(ravi[i][0])
	if(ravi[i][0]=='V'):
	#	print(ravi[i])
		for j in range(1,int(k)+1):
			#print(ravi[i][1])
			#print(ravi[j][0].venom)
			if(int(ravi[i][1])==ravi[j][0].venom):
					print(ravi[j][0].name)
	elif (ravi[i][0]=='L'):
		for j in range(1,int(k)+1):
			if(int(ravi[i][1])==ravi[j][0].length):
					print(ravi[j][0].name)


