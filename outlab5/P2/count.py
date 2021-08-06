#! /usr/bin/python

import sys
import csv
import requests 
from bs4 import BeautifulSoup


btechOne=requests.get("https://www.cse.iitb.ac.in/page222?batch=BTech1")
b1soup=BeautifulSoup(btechOne.content , "lxml")
b1count=0
for b1num in b1soup.find_all("a", string="Update"):
	b1count=b1count+1

btechTwo=requests.get("https://www.cse.iitb.ac.in/page222?batch=BTech2" )
b2soup=BeautifulSoup(btechTwo.content , "lxml")
b2count=0
for b2num in b2soup.find_all("a", string="Update"):
	b2count=b2count+1

btechThree=requests.get("https://www.cse.iitb.ac.in/page222?batch=BTech3")
b3soup=BeautifulSoup(btechThree.content , "lxml")
b3count=0
for b3num in b3soup.find_all("a", string="Update"):
	b3count=b3count+1

btechFour=requests.get("https://www.cse.iitb.ac.in/page222?batch=BTech4")
b4soup=BeautifulSoup(btechFour.content , "lxml")
b4count=0
for b4num in b4soup.find_all("a", string="Update"):
	b4count=b4count+1

dualFive=requests.get("https://www.cse.iitb.ac.in/page222?batch=DD5")
dualsoup=BeautifulSoup(dualFive.content , "lxml")
dualcount=0
for dualnum in dualsoup.find_all("a", string="Update"):
	dualcount=dualcount+1

mtechOne=requests.get("https://www.cse.iitb.ac.in/page222?batch=MTech1")
m1soup=BeautifulSoup(mtechOne.content , "lxml")
m1count=0
for m1num in m1soup.find_all("a", string="Update"):
	m1count=m1count+1

mtechTwo=requests.get("https://www.cse.iitb.ac.in/page222?batch=MTech2")
m2soup=BeautifulSoup(mtechTwo.content , "lxml")
m2count=0
for m2num in m2soup.find_all("a", string="Update"):
	m2count=m2count+1

mtechThree=requests.get("https://www.cse.iitb.ac.in/page222?batch=MTech3")
m3soup=BeautifulSoup(mtechThree.content , "lxml")
m3count=0
for m3num in m3soup.find_all("a", string="Update"):
	m3count=m3count+1

phd=requests.get("https://www.cse.iitb.ac.in/page222?batch=PhD")
phdsoup=BeautifulSoup(phd.content , "lxml")
phdcount=0
for phdnum in phdsoup.find_all("a", string="Update"):
	phdcount=phdcount+1

csvfile=open("count.csv" , "w+")
fieldnames=["Category name" , "No. of students"]
writer=csv.DictWriter(csvfile , fieldnames=fieldnames)
writer.writeheader()
writer.writerow({'Category name': "B.Tech - I" , 'No. of students': b1count })
writer.writerow({'Category name': "B.Tech - II" , 'No. of students': b2count })
writer.writerow({'Category name': "B.Tech - III" , 'No. of students': b3count })
writer.writerow({'Category name': "B.Tech - IV" , 'No. of students': b4count })
writer.writerow({'Category name': "Dual Degree - V" , 'No. of students': dualcount })
writer.writerow({'Category name': "M.Tech - I" , 'No. of students': m1count })
writer.writerow({'Category name': "M.Tech - II" , 'No. of students': m2count })
writer.writerow({'Category name': "M.Tech - III" , 'No. of students': m3count })
writer.writerow({'Category name': "Ph.D" , 'No. of students': phdcount })
csvfile.close()
