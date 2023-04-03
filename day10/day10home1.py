import sqlite3
import random
from mysql.connector import cursor
import json
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', user='vbm', password='!QA2ws3ed')
cursor = mydb.cursor()
query = "insert into tickets"
nonfirst = False


for ticket_id in range(1, 1000001):

    ticket_number = random.randint(1, 999999)

    mydb._execute_query("INSERT INTO db2064.ticket_line (ticket_number) VALUES ()")
    ticket_line_id = cursor.lastrowid

    numbers = random.sample(range(1, 46), 5)

    for number in numbers:
        mydb._execute_query(
            "INSERT INTO db2064.ticket_line_numbers (number, ticket_line_id) VALUES (?, ?)", (number, ticket_line_id))


mydb.commit()
mydb.close()
