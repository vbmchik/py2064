import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
squares1 = [1,3,7,12,21]
fig, ax = plt.subplots()

ax.plot(squares)
ax.plot(squares1)
plt.show()