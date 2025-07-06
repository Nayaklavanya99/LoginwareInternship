# Import required libraries for plotting
import matplotlib.pyplot as plt
# from sympy.abc import y
# from sympy.abc import x


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


fig, axs = plt.subplots(2, 2)

# Create subplots
axs[0, 0].plot(x, y)  
# axs[0, 0].set_title('Line 1')
# axs[0, 0].set_xlabel('x-axis')
# axs[0, 0].set_ylabel('y-axis')
axs[0, 1].scatter(y, x)    
# axs[0, 1].set_title('Line 2')
# axs[0, 1].set_xlabel('x-axis')
# axs[0, 1].set_ylabel('y-axis')
axs[1, 0].bar(y, x)
# axs[1, 0].set_title('Line 3')
# axs[1, 0].set_xlabel('x-axis')
# axs[1, 0].set_ylabel('y-axis')
axs[1, 1].hist(y)
# axs[1, 1].set_title('Line 4')
# axs[1, 1].set_xlabel('x-axis')
# axs[1, 1].set_ylabel('y-axis')
plt.show()
    

