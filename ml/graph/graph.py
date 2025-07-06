import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
fig,ax = plt.subplots(facecolor='brown')
# plt.scatter(x, y,color="red")
plt.plot(x, y, label='Line 1',color="green",marker="2",linestyle=":",linewidth=2,markerfacecolor="red",markeredgecolor="yellow")
plt.plot(y, x, label='Line 2',color="blue",marker="1",linestyle="--",linewidth=2,markerfacecolor="orange",markeredgecolor="purple")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Scatter Plot")
# plt.figure(figsize=(10, 5))
plt.grid(True)
plt.gca().set_facecolor('black')
plt.legend()
plt.show()
