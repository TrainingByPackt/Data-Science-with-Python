# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:11:41 2019

@author: aengland
"""

# data visualizations

# functional method

# Exercise 1: Line Plot

# create an array of numbers for x
import numpy as np
x = np.linspace(0, 10, 20)

# create y
y = x**3

# create y2
y2 = x**2

# create simple line plot
import matplotlib.pyplot as plt
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

# create a list of groups
x = ['Shirts', 'Pants','Shorts','Shoes']

# create a list of revenue
y = [1000, 1200, 800, 1800]

# create bar plot
import matplotlib.pyplot as plt
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
import matplotlib.pyplot as plt
plt.bar(x, y) # plot revenue by group
plt.xlabel('Item Type') # x-axis label
plt.ylabel('Sales Revenue ($)') # y-axis label
plt.title('{} Produce the Most Sales Revenue'.format(most_sold_item)) # create programmatic title
plt.show() # print the plot


# make a horizontal bar plot
import matplotlib.pyplot as plt
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

###############################################################################

# Exercise 4: Scatterplot

# 1. generate list of numbers for height
y = [5, 5.5, 5, 5.5, 6, 6.5, 6, 6.5, 7, 5.5, 5.25, 6, 5.25]

# 2. create a list of numbers for weight
x = [100, 150, 110, 140, 140, 170, 168, 165, 180, 125, 115, 155, 135]

# 3. create histogram
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.xlabel('Weight')
plt.ylabel('Height')
plt.show()


# 5. calculate pearson correlations
from scipy.stats import pearsonr
correlation_coeff, p_value = pearsonr(x, y)

# 6. Set up some logic
if correlation_coeff == 1.00:
    title = 'There is a perfect positive linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff >= 0.8:
    title = 'There is a very strong, positive linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff >= 0.6:
    title = 'There is a strong, positive linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff >= 0.4:
    title = 'There is a moderate, positive linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff >= 0.2:
    title = 'There is a weak, positive linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff > 0:
    title = 'There is a very weak, positive linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff == 0:
    title = 'There is no linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff <= -0.8:
    title = 'There is a very strong, negative linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff <= -0.6:
    title = 'There is a strong, negative linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff <= -0.4:
    title = 'There is a moderate, negative linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
elif correlation_coeff <= -0.2:
    title = 'There is a weak, negative linear relationship (r = {0:0.2f}).'.format(correlation_coeff)
else: 
    title = 'There is a very weak, negative linear relationship (r = {0:0.2f}).'.format(correlation_coeff)

# 7. Use title as title
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title(title)
plt.show()

###############################################################################

# Exercise 5: Box-and-Whisker plot

# 1. Generate a list of normally distributed numbers
import numpy as np
y = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1

# 2. Generate boxplot
import matplotlib.pyplot as plt
plt.boxplot(y)
plt.show()

# 3. Calculate shapiro wilk p-value
from scipy.stats import shapiro
shap_w, shap_p = shapiro(y)

# 4. Get outliers
# convert to z-scores
from scipy.stats import zscore
y_z_scores = zscore(y)

# 5. get the number of scores with absolute value of 3 or more
total_outliers = 0
for i in range(len(y_z_scores)):
    if abs(y_z_scores[i]) >= 3:
        total_outliers += 1
           
# 6. set up some logic for the title
if shap_p > 0.05:
    title = 'Normally distributed with {} outlier(s).'.format(total_outliers)
else:
    title = 'Not normally distributed with {} outlier(s).'.format(total_outliers)

# 7. Generate boxplot with programmatic tile
import matplotlib.pyplot as plt
plt.boxplot(y)
plt.title(title)
plt.show()


###############################################################################

# Exercise 5: Single Line Plot Using Subplots

import numpy as np
x = np.linspace(0, 10, 20)
# create y
y = x**3

# create plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots()
axes.plot(x, y, 'D-k')
axes.set_xlabel('Linearly Spaced Numbers')
axes.set_ylabel('y Value')
axes.set_title('As x increases, y increases by x cubed')
plt.show()

# call the plot object
fig

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

# call the object
fig


