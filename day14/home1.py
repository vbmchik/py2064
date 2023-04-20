from pprint import pprint
import mysql.connector as msql
import matplotlib.pyplot as plt
from mysql.connector import cursor
import json


def extract_business_data(dlist, businessid):
    res = filter(lambda x: x[2] == businessid, dlist)
    res = list(map(lambda x: (x[0] + " / " + x[1], x[3]), res))
    return res

fig, axs = plt.subplots(3, 1, figsize=(8, 12))
mydb = msql.connect(host="localhost", user="vbm", password="!QA2ws3ed")
cursor = mydb.cursor()

query = "select * from db2064.finances order by year"
cursor.execute(query)
result = list(cursor.fetchall())
cursor.close()
mydb.close()


for i in range(3):
    fig, axs = plt.subplots()
    bdata = extract_business_data(result, i+1)
    x = [m[0] for m in bdata ]
    y = [m[1] for m in bdata ]
    axs.plot(x, y, label=f'Бизнес {i+1}')
    axs.set_xlabel('Год и месяц')
    axs.set_ylabel('Доход')
    axs.set_title(f'График доходов Бизнес {i+1}')
    axs.tick_params(axis='x', rotation=90)
    
plt.show()