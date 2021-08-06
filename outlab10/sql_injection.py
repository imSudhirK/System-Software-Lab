import sqlite3
from sqlite3 import Error
import sys

ipldb = sqlite3.connect('ipl.db')
cur = ipldb.cursor()
firstArgv = int (input())
if firstArgv == 1 :
    secondArgv = int( input())
    if secondArgv == 1:
        string=input()
        a=" "
        cur.execute("""DELETE FROM TEAM WHERE team_name = ?""", (string,))
        ipldb.commit()
        cur.execute('''SELECT * FROM TEAM''')      
    elif (secondArgv == 0):
        ipldb.text_factory = str
        myInput = str(input())
        query = "DELETE FROM TEAM WHERE team_name = '%s';" % myInput.strip()
        mydata = cur.execute(query)
        ipldb.commit()
        cur.execute('''SELECT * FROM TEAM''')      
    ipldb.close()
elif firstArgv == 2 :
    secondArgv = int( input())
    if secondArgv == 1 :
        string=input()
        a=" "
        cur.execute("""DELETE FROM PLAYER WHERE player_name = ?""", (string,))
        ipldb.commit()
        cur.execute('''SELECT * FROM PLAYER''')
    elif secondArgv == 0:
        ipldb.text_factory = str 
        myInput = str(input())
        query = "DELETE FROM TEAM WHERE player_name = '%s';" % myInput.strip()
        mydata = cur.execute(query)
        ipldb.commit()
        cur.execute('''SELECT * FROM TEAM''')
    ipldb.close()
elif firstArgv == 3 :
    secondArgv = int( input())
    if secondArgv == 1:
        string=int(input())
        a=" "
        cur.execute("""DELETE FROM MATCH WHERE match_id = ?""", (string,))
        ipldb.commit()
        cur.execute('''SELECT * FROM MATCH''')
    elif secondArgv == 0:
        ipldb.text_factory = str 
        myInput = int(input())
        query = "DELETE FROM TEAM WHERE match_id = '%s';" % myInput.strip()
        mydata = cur.execute(query)
        ipldb.commit()
        cur.execute('''SELECT * FROM TEAM''')
    ipldb.close()
