import matplotlib.pyplot as plt



# giwe x y list
#make x random
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

fig,ax = plt.subplots(facecolor='brown')
# plt.scatter(x, y,color="red")
plt.plot(x, y, label='data',color="green",marker="*",linestyle=":",linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
# plt.figure(figsize=(10, 5))
plt.grid(True)
plt.gca().set_facecolor('black')
plt.show()