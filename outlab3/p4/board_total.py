#! /usr/bin/env python

import sys

f=open("students.txt",'rU')
lines=f.readlines()
dict=[]

for line in lines:
	words=line.split()
	dict.append(words)

def find_total(x1, y1, x2, y2):
     count=0
     if x1 == x2:
         for i in range(1,int(dict[0][0])+1):
	     x=int(dict[i][0])
	     y=int(dict[i][1])
             if x == x1 :
                 count+=1
             else:
                 count+=0
     else:
          for i in range(1,int(dict[0][0])+1):
	      x=int(dict[i][0])
	      y=int(dict[i][1])
              M= (y1-y2)/(x1 - x2)
              if (x == x1 and y == y1):
                  count+=1
              elif (y-y1)/(x-x1) == M:
                  count+=1
              else:
                  count+=0
     return count

x1,y1,x2,y2=map(int,raw_input().split())

print find_total(x1, y1, x2, y2)


