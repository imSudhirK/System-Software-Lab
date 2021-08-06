from __future__ import print_function
import sqlite3



from operator import itemgetter
ipldb = sqlite3.connect('ipl.db')
cur = ipldb.cursor()
a=[]
cur.execute('''SELECT player_name,player_id FROM PLAYER ''')
d=1
for row in cur:
    a.append([d,row[0],0,0,0])	
    d=d+1
cur.execute('''SELECT striker,runs_scored FROM BALL_BY_BALL ''')
for row in cur:
    a[int(row[0])-1][3]=a[int(row[0])-1][3]+1
    if(int(row[1])==6):
        a[int(row[0])-1][2]=a[int(row[0])-1][2]+1
for i in range(0,d-1):
    if(a[i][3]!=0):
        a[i][4]=float(a[i][2])/a[i][3]
    else:
        a[i][4]=0   
a=sorted(a, key=itemgetter(4),reverse=True)
for i in range(0,d-1):
    if(a[i][3]!=0):    
        print(*a[i], sep=",")
ipldb.close()
