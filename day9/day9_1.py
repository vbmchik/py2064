from pprint import pprint
from mysql.connector import cursor
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = mydb.cursor()
query = "select * from db2064.cats ;"
# where color <> 'black' and age > 2 and price < 2500
cursor.execute(query)
result = cursor.fetchall()
cursor.close()
mydb.close()

result = list(filter(lambda x: x[2] != 'Black' and x[4] > 2 and x[5] < 2500, result))
result.sort(key=lambda x: x[5])

pprint(result)

