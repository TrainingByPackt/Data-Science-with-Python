# Activity 1: Line Plot

# Create x
x = ['January','February','March','April','May','June']
print(x)

# Create y
y = [1000, 1200, 1400, 1600, 1800, 2000]
print(y)

# Create the plot
import matplotlib.pyplot as plt # import matplotlib
plt.plot(x, y, '*:b') # plot items sold (y) by month (x)
plt.xlabel('Month') # label x-axis
plt.ylabel('Items Sold') # label y-axis
plt.title('Items Sold has been Increasing Linearly') # add plot title
plt.show() # print plot