from itertools import groupby
from mysql.connector import cursor
import mysql.connector

def makecortage(y):
    l = []
    for a, b in y:
        l.append(b)
    l.sort()
    return tuple(l) 

mydb = mysql.connector.connect(
    host='localhost', user='vbm', password='!QA2ws3ed')
cursor = mydb.cursor()

winning = (11, 22, 13, 14, 15)

query = "select ticket_line.number as line_number,  ticket_line_numbers.number from db2064.ticket_line left join db2064.ticket_line_numbers on ticket_line.id = ticket_line_numbers.ticket_line_id order by ticket_line.number"

cursor.execute(query)
winners = cursor.fetchall()
cursor.close()
mydb.close()

#windic = { a: makecortage(b) for a, b in groupby(winners, lambda x: x[0])  }
windic = { a: tuple([ a[1] for a in b]) for a, b in groupby(winners, lambda x: x[0]) }

winlines = []
for key, value in windic.items():
    s = set(value) & set(winning)
    if len(s) >= 3:
        winlines.append((key, set(value) & set(winning)))
    
print(len(winlines))
