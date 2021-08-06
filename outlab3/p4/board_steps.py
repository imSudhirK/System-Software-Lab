#! /usr/bin/python

import sys
f=open("students.txt",'rU')
lines=f.readlines()
dict=[]

for line in lines:
	words=line.split()
	dict.append(words)
def find_loc(x1 ,y1 ,x2 , y2):
        if (x1>x2 | y1> y2 ):
            print   -1
        else :
            print x2+y2-x1-y1

    
x1=int(raw_input ("Enter x1: ") )
y1=int(raw_input ("Enter y1: "))
x2=int(raw_input ("Enter x2: "))
y2=int(raw_input ("Enter y2: "))

find_loc(x1 ,y1 ,x2 , y2)

