from __future__ import print_function
import sqlite3
from operator import itemgetter
from typing import List, Any, Union

ipldb = sqlite3.connect('ipl.db')
cur = ipldb.cursor()
a=[]
b=[]
cur.execute('''SELECT player_name,player_id FROM PLAYER ''')
d=1
for row in cur:
    a.append([d,row[0],0,0,0])
    b.append([])
    d=d+1
cur.execute('''SELECT striker,match_id FROM BALL_BY_BALL ''')
for row in cur:
    if int(row[1]) not in b[int(row[0])-1]:
        b[int(row[0])-1].append(int(row[1]))
        a[int(row[0])-1][3]=a[int(row[0])-1][3]+1
        a[int(row[0])-1][2] = a[int(row[0])-1][2] + 1
    elif int(row[1]) in b[int(row[0])-1]:
        a[int(row[0])-1][2] = a[int(row[0])-1][2] + 1
for i in range(0,d-1):
    if(a[i][3]==0):
        a[i][4]=0
    else:
        a[i][4]=float(a[i][2])/a[i][3]
a=sorted(a, key=itemgetter(4),reverse=True)
q=0
s=0
for i in range(0,d-1):  # type:
    if (q >= 10):
        break
    if (s == 0):
        string=''
        string=string+str(a[i][0])+','+str(a[i][1])+','+str(a[i][4])
        print(string)
        s = s + 1
    else:
        string = ''
        string = string + str(a[i][0]) + ',' + str(a[i][1]) + ',' + str(a[i][4])
        print(string)
        if (a[i][4]!= a[i+1][4]):
            q = q + 1
ipldb.close()
