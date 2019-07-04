# Exercise 3: Bar Plot

# create a list of groups
x = ['Shirts', 'Pants','Shorts','Shoes']
print(x)

# create a list of revenue
y = [1000, 1200, 800, 1800]
print(y)

# create bar plot
import matplotlib.pyplot as plt
plt.bar(x, y) # plot revenue by group
plt.show()

# style the plot
import matplotlib.pyplot as plt
plt.bar(x, y) # plot revenue by group
plt.xlabel('Item Type') # x-axis label
plt.ylabel('Sales Revenue ($)') # y-axis label
plt.title('Sales Revenue by Item Type')
plt.show() # print the plot

# find the index of the greatest value in list y
index_of_max_y = y.index(max(y))
print(index_of_max_y)

# determine the most sold item
most_sold_item = x[index_of_max_y]
print(most_sold_item)

# make the title programmatic
import matplotlib.pyplot as plt
plt.bar(x, y) # plot revenue by group
plt.xlabel('Item Type') # x-axis label
plt.ylabel('Sales Revenue ($)') # y-axis label
plt.title('{} Produce the Most Sales Revenue'.format(most_sold_item)) # create programmatic title
plt.show() # print the plot

# make a horizontal bar plot
import matplotlib.pyplot as plt
plt.barh(x, y) # turn the plot horizontal
plt.xlabel('Item Type') # x-axis label
plt.ylabel('Sales Revenue ($)') # y-axis label
plt.title('{} Produce the Most Sales Revenue'.format(most_sold_item)) # create programmatic title
plt.show() # print the plot

# switch the axes labels
import matplotlib.pyplot as plt
plt.barh(x, y) # turn the plot horizontal
plt.xlabel('Sales Revenue ($)') # x-axis label
plt.ylabel('Item Type') # y-axis label
plt.title('{} Produce the Most Sales Revenue'.format(most_sold_item)) # create programmatic title
plt.show() # print the plot














