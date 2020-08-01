import sys
import math
def sidelength(p1,q1,p2,q2):
    length = math.sqrt((p1-p2)**2+(q1-q2)**2)
    return length
def areaoftriangle( x1,y1,x2,y2,x3,y3 ):
    a=sidelength( x1,y1,x2,y2 )
    b=sidelength( x2,y2,x3,y3 )
    c=sidelength( x1,y1,x3,y3 )
    s=(a+b+c)/2
    area=math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return area
def insideOut(x1,y1,x2,y2,x3,y3,x,y):
	e = areaoftriangle(x1,y1,x2,y2,x,y)
	f = areaoftriangle(x3,y3,x2,y2,x,y)
	g = areaoftriangle(x1,y1,x3,y3,x,y)
	h = float(areaoftriangle(x1,y1,x3,y3,x2,y2))
	sum1 = float(e+f+g)
        if str(sum1) == str(h):
            
	    c = "INSIDE"
	   
	else:
            c = "OUTSIDE"
        print c
	return c
x1,y1=map(int,raw_input("Enter the first coordinate :").split())
x2,y2=map(int,raw_input("Enter the second coordinate :").split())
x3,y3=map(int,raw_input("Enter the thirdc coordinate :").split())
x,y=map(float,raw_input("Enter coordinates of the key :").split())
print insideOut(x1,y1,x2,y2,x3,y3,x,y)

