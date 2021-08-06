#!/usr/bin/python3
import sys
import csv
import sqlite3

Connect = sqlite3.connect("cse_students.sqlite")
Cursor = Connect.cursor()
Cursor.execute("CREATE TABLE t ('Category name', 'No. of students');") 

with open('count.csv','rt') as sdr: 
    dr = csv.DictReader(sdr) 
    next(dr)
    to_db = [(i['Category name'], i['No. of students']) for i in dr]

Cursor.executemany("INSERT INTO t ('Category name', 'No. of students') VALUES (?, ?);", to_db)
Connect.commit()
Connect.close()

conn = sqlite3.connect('cse_students.sqlite')
cursor = conn.execute("SELECT 'Category name', 'No. of students' from t")

conn.close()


course=str(input("Enter the category  name : "))

