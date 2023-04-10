from mysql.connector import cursor
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost', user='vbm', password='!QA2ws3ed')
cursor = mydb.cursor()

winning = (11,22,13,14,15)

""" select ticket_line_id, GROUP_CONCAT(number order by number)  FROM
ticket_line_numbers
where number in (3, 12, 32, 21, 3)
GROUP BY ticket_line_id
having count(*) >= 3 order by count(*) desc """

query = f"select ticket_line_id, GROUP_CONCAT(number order by number) FROM "
query += f"db2064.ticket_line_numbers where number in " + str(winning)
query += " GROUP BY ticket_line_id having count(*) >= 3 order by count(*) desc "

cursor.execute(query)
winners = cursor.fetchall()
cursor.close()
mydb.close()

winners.sort(key=lambda x: x[0])
print(len(winners))
