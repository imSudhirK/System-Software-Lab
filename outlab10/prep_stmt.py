import sqlite3
import sys
ipldb = sqlite3.connect('ipl.db')
cur = ipldb.cursor()
l=['TEAM','PLAYER','MATCH','PLAYER_MATCH','BALL_BY_BALL']
n=['VALUES (?, ?)',' VALUES (?, ?, ?, ?, ?, ?)','VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)','VALUES (?, ?, ?, ?, ?, ?, ?)','VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)']
r2=int(input())
r=[]
n1=[2,6,15,7,11]
p=l[r2-1]
q=n[r2-1]
if(n1[r2-1]==2):
    r1=int(input())
    r.append(r1) 
    r2=input()
    r.append(r2)
elif(n1[r2-1]==15):
    for i in range(0,6):
        r1=int(input())
        r.append(r1) 
    for i in range(0,3):
        r2=input()
        r.append(r2)
    for i in range(0,2):
        r3=int(input())
        r.append(r3)
    for i in range(0,2):
        r4=input()
        r.append(r4)
    for i in range(0,2):
        r5=int(input())
        r.append(r5)
elif(n1[r2-1]==6):
    r1=int(input())
    r.append(r1)
    for i in range(0,5):
        r2=input()
        r.append(r2)
elif(n1[r2-1]==7):
    for i in range(0,3):
        r2=int(input())
        r.append(r2)
    for i in range(0,3):
        r3=input()
        r.append(r3)
    r3=int(input())
    r.append(r3)
elif(n1[r2-1]==11):
    for i in range(0,7):
        r2=int(input())
        r.append(r2)
    r3=input()
    r.append(r3)
    for i in range(0,3):
        r4=int(input())
        r.append(r4)

        
cur.execute("""INSERT INTO """+p+""" """+q+""" """,r)
ipldb.commit()
r=[]
ipldb.close()
