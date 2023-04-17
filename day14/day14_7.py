import matplotlib.pyplot as plt

x = list(range(1,1001))
y = list(map(lambda y: y**2, x))

fig, axe = plt.subplots()
axe.scatter(x,y,c=y,cmap=plt.cm.Blues, s = 5)
plt.show()