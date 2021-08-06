import sqlite3
ipldb = sqlite3.connect('ipl.db')
cur = ipldb.cursor()
a={}
b={}

cur.execute('''
	SELECT venue_name,count(*) FROM MATCH GROUP BY venue_name''')
for row in cur:
	a[row[0]]=row[1]
cur.execute('''
	SELECT venue_name,sum(runs_scored)
	FROM BALL_BY_BALL 
	INNER JOIN MATCH ON BALL_BY_BALL.match_id=MATCH.match_id
	GROUP BY
	venue_name''')
for row in cur:
	b[row[0]]=row[1]/a[row[0]]
c=sorted(b, key=b.get,reverse=True)


for r in c:
	print("{},{}".format(r,b[r]))

ipldb.close()