# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:11:41 2019

@author: aengland
"""

# data visualizations

# functional method

# Exercise 1: Line Plot
import matplotlib.pyplot as plt

# create an array of numbers for x
import numpy as np
x = np.linspace(0, 10, 20)

# create y
y = x**3

# create y2
y2 = x**2

# create simple line plot
plt.figure(figsize=(10,5)) # increase plot size
plt.plot(x, y, 'D-k', label='x cubed') # label as x cubed
plt.plot(x, y2, '--r', label='x squared') # label as x squared
plt.xlabel('Linearly Spaced Numbers') # add x axis label
plt.ylabel('y Value')
plt.title('As x increases, \nx Cubed (black) increases \nat a Greater Rate than \nx Squared (red)', fontsize=22) # make a multi-line title
plt.legend(loc='upper left') # create a plot legend and place it in the upper left
plt.show() # print the plot

###############################################################################

# Exercise 2: Bar Plot
import matplotlib.pyplot as plt

# create a list of groups
x = ['Shirts', 'Pants','Shorts','Shoes']

# create a list of revenue
y = [1000, 1200, 800, 1800]

# create bar plot
plt.bar(x, y) # plot revenue by group
plt.xlabel('Item Type') # x-axis label
plt.ylabel('Sales Revenue ($)') # y-axis label
plt.title('Sales Revenue by Item Type')
plt.show() # print the plot

# find the index of the greatest value in list y
index_of_max_y = y.index(max(y))

# determine the most sold item
most_sold_item = x[index_of_max_y]
print(most_sold_item)

# make the title programmatic
plt.bar(x, y) # plot revenue by group
plt.xlabel('Item Type') # x-axis label
plt.ylabel('Sales Revenue ($)') # y-axis label
plt.title('{} Produce the Most Sales Revenue'.format(most_sold_item)) # create programmatic title
plt.show() # print the plot


# make a horizontal bar plot
plt.barh(x, y) # plot revenue by group
plt.xlabel('Sales Revenue ($)') # x-axis label
plt.ylabel('Item Type') # y-axis label
plt.title('{} Produce the Most Sales Revenue'.format(most_sold_item)) # create programmatic title
plt.show() # print the plot

###############################################################################

# Exercise 3: Histogram

# generate list of normally distributed numbers
import numpy as np
y = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1

# create histogram
import matplotlib.pyplot as plt
plt.hist(y, bins=20)
plt.show()

# run the shapiro wilk test
from scipy.stats import shapiro
shap_w, shap_p = shapiro(y)
print(shap_p)

# set up some logic
if shap_p > 0.05:
    normal_YN = 'Fail to reject the null hypothesis. Data is normally distributed.'
else:
    normal_YN = 'Null hypothesis is rejected. Data is not normally distributed.'
print(normal_YN)

# re-create histogram
import matplotlib.pyplot as plt
plt.hist(y, bins=20)
plt.xlabel('y Value')
plt.ylabel('Frequency')
plt.title(normal_YN) # programmatic plot title
plt.show()











# using subplots

# Exercise 4:Single Line Plot Using Subplots

import numpy as np
x = np.linspace(0, 10, 20)
# create y
y = x**3

import matplotlib.pyplot as plt
fig, axes = plt.subplots()
axes.plot(x, y, 'D-k')
axes.set_xlabel('Linearly Spaced Numbers')
axes.set_ylabel('y Value')
axes.set_title('As x increases, y increases by x cubed')
plt.show()

###############################################################################

# Exercise 5: Multiple Line Plots Using Subplots
import numpy as np
x = np.linspace(0, 10, 20)
# create y
y = x**3
# create y2
y2 = x**2

# create 1 row of 2 subplots
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y) # plot x-cubed by x
axes[0].set_title('x by x Cubed') # set title
axes[0].set_xlabel('Linearly Spaced Numbers') # set x axis label
axes[0].set_ylabel('y Value') # set y axis label
# plot on the right axes
axes[1].plot(x, y2) # plot x-squared by x
axes[1].set_title('x by x Squared') # set title
axes[1].set_xlabel('Linearly Spaced Numbers') # set x axis label
axes[1].set_ylabel('y Value') # set y axis label
plt.tight_layout() # prevent plot overlap
plt.show()

axes[0].plot(x, y)



for current_ax in axes:
    current_ax.plot(x, y, 'D-k')
    plt.tight_layout()
    

axes[0].plot(x, y)
fig



