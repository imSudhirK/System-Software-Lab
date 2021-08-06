#! /usr/bin/env python
import random
import pickle
import string
a = random.sample(range(1,5000),100)
def random_strings(size=4,chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
b = list()
while len(b) < 100:
    b.append(random_strings())
concat_func = lambda x,y: x + " " + str(y)
c = list(map(concat_func,b,a))
file = open('new_int', 'wb')
pickle.dump(c, file)
file.close()
d = int(raw_input("Enter Number:"))
e = -1
f = []
g = []
def h(x):
    for i in range(0,99):
        if (x == a[i]):
            return i
for i in a:
    e = e+1  
    if (d-i) in a:
        f.append(c[e])
        f.append(c[h(d-i)])
for i in range(0,98):
    for m in range(i+1,99):
        if (a[i]+a[m] < d):
            g.append(c[i])
            g.append(c[m])
if (len(f) != 0):
    print f[0],f[1]
else:
    print g[0],g[1]


    

        

