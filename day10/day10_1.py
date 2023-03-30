from pprint import pprint
import random
from mysql.connector import cursor
import json
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()
query = "insert into db2064.myrecords (summa) values "
nonfirst = False
n = 0
for _ in range(1000111):
    x = random.randint(1, 100)
    if nonfirst:
        query += ", "
    nonfirst = True
    query += f"({x})"
    n += 1
    if n == 1000:
        cursor.execute(query)
        mydb.commit()
        print("Write committed!")
        query = "insert into db2064.myrecords (summa) values "
        nonfirst = False
        n = 0
if n > 0:
    cursor.execute(query)
    mydb.commit()

cursor.close()
mydb.close()
# where color <> 'black' and age > 2 and price < 2500
