import matplotlib.pyplot as plt

x = [
    (2002, 1, 1),
    (2002, 2, 1),
    (2002, 3, 1),
    (2002, 4, 1)
]

x1 = list(map(lambda y: str(y[0]) + "/" + str(y[1]), x))
y = [1200, 900, 1300, 1400]
y1 = [200, 200, 500, 800]
y2 = [800, 900, 1500, 1800]
y3 = [100, 200, 700, 900]
fig, axe = plt.subplots(2,2)
axe[0][0].plot(x1,y,linewidth=2)
axe[0][1].plot(x1,y1,linewidth=2)
axe[1][0].plot(x1,y2,linewidth=2)
axe[1][1].plot(x1,y3,linewidth=2)
axe[1][0].annotate("best value", xy = (3.0, 1800), xytext=(3, 1870), arrowprops=dict(arrowstyle='->', facecolor='green'))

plt.show()