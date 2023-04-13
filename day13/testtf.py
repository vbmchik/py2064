from tensorflow import *
from keras import *
from keras import layers

model = models.Sequential()
input_list = [1, 2, 3, 4, 5]
output_list = [9, 14, 19, 24, 29]
# output_list = [3,6,9,12,15]
model.add(layers.Dense(units=5, input_shape=[1]))
model.add(layers.Dense(units=400, input_shape=[1]))
model.add(layers.Dense(units=1800, input_shape=[1]))
model.add(layers.Dense(units=500, input_shape=[1]))
model.add(layers.Dense(units=1, input_shape=[1]))
model.compile(loss="mean_squared_error", optimizer="adam")
model.fit(x=input_list, y=output_list, epochs=1000)
print(model.predict([6, 200, 1225, 7]))
