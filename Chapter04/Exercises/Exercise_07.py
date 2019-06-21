# Exercise 7: Single Line Plot Using Subplots

import numpy as np
x = np.linspace(0, 10, 20) # create x
y = x**3 # create y

# create figure and a set of axes
import matplotlib.pyplot as plt # import dependencies
fig, axes = plt.subplots() # create figure and set of axes
plt.show() # print plot

# call the plot object
fig

# create a line plot in the axes
import matplotlib.pyplot as plt # import dependencies
fig, axes = plt.subplots() # create figure and set of axes
axes.plot(x, y) # generate line
plt.show() # print plot

# create styled plot
import matplotlib.pyplot as plt # import matplotlib
fig, axes = plt.subplots() # create figure and axes
axes.plot(x, y, 'D-k') # create black line with diamond markers
axes.set_xlabel('Linearly Spaced Numbers') # x label
axes.set_ylabel('y Value') # y label
axes.set_title('As x increases, y increases by x cubed') # set title
plt.show() # print plot

# call the plot object
fig