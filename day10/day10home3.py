import sqlite3
import random
from mysql.connector import cursor
import json
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', user='vbm', password='!QA2ws3ed')
cursor = mydb.cursor()

for i in range(100000):
    query = f"insert into db2064.ticket_line (number) values({i+1})"
    cursor.execute(query)
    mydb.commit()
    id = cursor.lastrowid
    l = []
    while len(l) < 5:
        t = random.randint(1,45)
        if t not in l:
            l.append(t)
    for x in l:
        query = f"insert into db2064.ticket_line_numbers (number, ticket_line_id) values({x}, {id})"
        cursor.execute(query)
        mydb.commit()
