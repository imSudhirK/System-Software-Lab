#! /usr/bin/python3
import csv, os ,collections
import matplotlib.pyplot as plt
import pandas as pd
from pylab import *

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

csvfile = open ("d1131.csv" ,  "w+")
fieldnames = [ 'topic' , 'Essential', 'Nice to have' , 'Dont care one way or another', 'Utterly useless' ]
writer = csv.DictWriter(csvfile , fieldnames= fieldnames)
writer.writeheader()
for i in range(1, 29):
	freq = fun(i)
	writer.writerow({ 'topic':Topic[i-1],'Essential': freq['Essential'] ,'Nice to have': freq['Nice to have'], 'Dont care one way or another' : freq['Dont care one way or another'] , 'Utterly useless': freq['Utterly useless']  })
csvfile.close()

df1 =pd.read_csv("d1131.csv", index_col=0) 
os.remove('d1131.csv')   
colors=["blue","cyan","yellow","red"]
df1.plot(kind='bar', stacked=True, color=colors, linewidth=0.5, alpha= 1); 
plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.15),ncol=2)
savefig('hists.png',figsize=(100, 100), dpi=800, bbox_inches=None, pad_inches=0.1)


