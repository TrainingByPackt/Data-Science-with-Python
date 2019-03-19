# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:11:41 2019

@author: aengland
"""

# data visualizations

# functional method

# Exercise 1: 
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


# Activity 1:

# Exercise 2:

# Activity 2:
###############################################################################


# using subplots

# Exercise 3:

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






for current_ax in axes:
    current_ax.plot(x, y, 'D-k')
    plt.tight_layout()
    

axes[0].plot(x, y)
fig



