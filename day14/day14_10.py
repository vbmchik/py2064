import matplotlib.pyplot as plt

x = list(range(-100, 101))
y = [(100**2-t**2)**0.5 for t in x]
y1 = [ -x for x in y ]
#x.extend(x)
x.extend(range(100, -101, -1))
y.extend(y1)
fig, axs = plt.subplots()
axs.plot(x,y)
#axs.plot(x, y1)
plt.show()