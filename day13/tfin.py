from pprint import pprint
import mysql.connector
import numpy
from keras import *
from keras import layers

incomesdb = mysql.connector.connect(
    host='localhost', user='user2064', password='!QA2ws3ed')
cursor = incomesdb.cursor()
query = "select age, education_years, work_experience, country, salary_month from db2064.incomes"
cursor.execute(query)
dataincomes = numpy.array(cursor.fetchall())

input = dataincomes[0:8, 0:4]
output = dataincomes[0:8, 4]
model = models.Sequential()
model.add(layers.Dense(units=16, input_shape=[4]))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=256))
model.add(layers.Dense(units=32))
model.add(layers.Dense(units=1))
model.compile(optimizer="adam", loss="mean_squared_error")
model.fit(x=input, y = output, epochs=5000)
pprint(dataincomes)
jjj = numpy.array([[50,7,17,2],[50,7,17,1]])
pprint(model.predict(jjj))