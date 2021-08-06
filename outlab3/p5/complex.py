#!/usr/bin/env python
import sys
import math
f = open("numbers.txt",'rU')
k = []
l = []
lines = f.readlines()
for line in lines:
    words = line.split()
    for word in words:
        k.append(int (word))
	l.append(float (word))
class complex(object):
    def __init__(self,re,im):
        self.re = re
        self.im = im
    def str(self):
        if self.im <= 0:
            if self.im == 0:
                print self.re
            else:
                print self.re,"-",(-1 * self.im),"i"
        else:    
            print self.re,"+",self.im,"i"
    def add(self,rhs):
        new_a = self.re + rhs.re
        new_b = self.im + rhs.im
        if new_b <= 0:
            if new_b == 0:
                print new_a
            else:
                print new_a,"-",(-1 * new_b),"i"
        else:    
            print new_a,"+",new_b,"i"
    def sub(self,rhs):
        new_a = self.re - rhs.re
        new_b = self.im - rhs.im
        if new_b <= 0:
            if new_b == 0:
                print new_a
            else:
                print new_a,"-",(-1 * new_b),"i"
        else:    
            print new_a,"+",new_b,"i"
    def mul(self,rhs):
        new_a = (self.re * rhs.re) - (self.im * rhs.im)
        new_b = (self.re * rhs.im) + (self.im * rhs.re)
        if new_b <= 0:
            if new_b == 0:
                print new_a
            else:
                print new_a,"-",(-1 * new_b),"i"
        else:    
            print new_a,"+",new_b,"i"
    def div(self,rhs):
        new_a = ((self.re * rhs.re) + (self.im * rhs.im))/(rhs.re * rhs.re + rhs.im * rhs.im)
        new_b = ((self.im * rhs.re) - (self.re * rhs.im))/(rhs.re * rhs.re + rhs.im * rhs.im)
        if new_b <= 0:
            if new_b == 0:
                print new_a
            else:
                print new_a,"-",(-1 * new_b),"i"
        else:    
            print new_a,"+",new_b,"i"
        
a = complex(k[0],k[1])
b = complex(k[2],k[3])
a.str()
b.str()
a.add(b)
a.sub(b)
a.mul(b)
a = complex(l[0],l[1])
b = complex(l[2],l[3])
a.div(b)
