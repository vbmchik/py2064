from plotly.graph_objects import Bar, Layout
import matplotlib.pyplot as plt
import seaborn as sn 
import numpy as np

years = [1998, 1999, 2000, 2001, 2002, 2003, 2004]
incomes=[1000000, 1500000, 1700000, 2300000, 2800000, 3200000, 4500000]
fig, axs = plt.subplots(1,1)
axs.scatter(x=years, y=incomes)
axs.bar(years, height=incomes)
axs.plot(years,incomes)
plt.show()