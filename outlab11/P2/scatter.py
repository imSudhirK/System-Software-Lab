
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1=[]
y1=[]
z1=[]
a=2
b=1
with open('3dpd.out','r') as f:
    for l in f:
    	row = l.split(',')
    	x1.append(float(row[0]))
    	y1.append(float(row[1]))
    	z1.append(float(row[2]))
 

ax.scatter(x1, y1, z1, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()