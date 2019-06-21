# Exercise 8: Multiple Line Plots Using Subplots

import numpy as np
x = np.linspace(0, 10, 20) # create x
y = x**3 # create y
y2 = x**2 # create y2

# create figure object with two subplots that are side-by-side
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=1, ncols=2)

# plot x on left axes
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y) # plot x squared by y

# add title and axis labels for left axes
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y) # plot x squared by y
axes[0].set_title('x by x Cubed') # set title
axes[0].set_xlabel('Linearly Spaced Numbers') # set x axis label
axes[0].set_ylabel('y Value') # set y axis label

# style the right axes
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

# prevent plot overlap
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

# call the object
fig