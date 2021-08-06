
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1=[]
y1=[]
z1=[]
x2=[]
y2=[]
z2=[]
a=-1
b=-1.2
c=4.3
with open('3dpd.out','r') as f:
    for l in f:
    	row = l.split(',')
    	if((a*float(row[2])+b*((float(row[0])*float(row[0]))+(float(row[1])*float(row[1])))+c)>=0):
    		x1.append(float(row[0]))
    		y1.append(float(row[1]))
    		z1.append(float(row[2]))
    	else:
    		x2.append(float(row[0]))
    		y2.append(float(row[1]))
    		z2.append(float(row[2]))

ax.scatter(x1, y1, z1, c='r', marker='o')
ax.scatter(x2, y2, z2, c='b', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
