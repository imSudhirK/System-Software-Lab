#! /usr/bin/python3

import csv, os, math
import collections
import numpy as np                                                               
import matplotlib.pyplot as plt  


csvReader = open ("survey_data.csv" ,"rU")
handle = csv.reader(csvReader)
Topic = []
for line in handle:
	for i in range(1,29):
		Topic.append(line[i])
	break 
csvReader.close()

def fun(i):
	csvReader = open ("survey_data.csv" ,"rU")
	handle = csv.reader(csvReader)
	A= collections.Counter()
	for row in handle:
		A[row[i]] += 1
	return A

def plog(x):
	l2 = 0.0
	if(x ==0):
		return l2
	else :
		l2 = math.log(x)/math.log(2.0)
		return x*l2
def entropy(t_freq):
	pE = t_freq['Essential']/ 13.0
	pN = t_freq['Nice to have']/13.0
	pD = t_freq['Dont care one way or another']/13.0
	pU = t_freq['Utterly useless']/13.0
	ans = 0.0
	ans = ans - plog(pE) - plog(pN) - plog(pD) - plog(pU)
	return  ans

csvfile = open ("d1132.csv" ,  "w+")
fieldnames = [ 'topic' , 'Entropy' ]
writer = csv.DictWriter(csvfile , fieldnames= fieldnames)
writer.writeheader()
for i in range(1, 29):
	freq = fun(i)
	Ent = entropy(freq)
	writer.writerow({ 'topic':Topic[i-1], 'Entropy': Ent })
csvfile.close()

import operator
csvReader1 = open ("d1132.csv" ,"rU")
handle1 = csv.reader(csvReader1)
next(handle1)
sortedlist = sorted(handle1, key=operator.itemgetter(1), reverse=True)
csvReader1.close()
os.remove('d1132.csv')
xs, ys = [*zip(*sortedlist)]
x_axix = list(np.array(xs))
y_axix = list(np.array(ys))
y_axix = list(map(float,y_axix))

sudhir =[]
for i in range(1, 29):
	sudhir.append(i)
plt.barh(sudhir,y_axix,align='center')
plt.yticks(sudhir, x_axix)
plt.savefig('cotr.png')
