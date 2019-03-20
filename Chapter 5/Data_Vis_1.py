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

# Activity 1: Line Plot

# 1. import matplotlib

# 2. Create x
x = ['January','February','March','April','May','June']

# 3. Create y
y = [1000, 1200, 1400, 1600, 1800, 2000]

# 4. Create the plot
import matplotlib.pyplot as plt
plt.plot(x, y, '*:b')
plt.xlabel('Month')
plt.ylabel('Items Sold')
plt.title('Items Sold has been Increasing Linearly')
plt.show()

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

# Activity 2: Bar plot

# 1. Import matplotlib

# 2. Create a list for x
x = ['Boston Celtics','Los Angeles Lakers', 'Chicago Bulls', 'Golden State Warriors', 'San Antonio Spurs']

# 3. Create a list for y
y = [17, 16, 6, 6, 5]

# 4. Put into a data frame so we can sort them
import pandas as pd
df = pd.DataFrame({'Team': x,
                   'Titles': y})

# 5. Sort df by titles
df_sorted = df.sort_values(by=('Titles'), ascending=False)

# 6. Make a programmatic title
# get team with most titles
team_with_most_titles = df_sorted['Team'][0]
# get the number of max titles
most_titles = df_sorted['Titles'][0]
# create title
title = 'The {} have the most titles with {}'.format(team_with_most_titles, most_titles)

# 6. Plot it
import matplotlib.pyplot as plt
plt.bar(df_sorted['Team'], df_sorted['Titles'], color='red')
plt.xlabel('Team')
plt.ylabel('Number of Championships')
plt.xticks(rotation=45)
plt.title(title)
plt.savefig('Titles_by_Team.jpeg')
plt.show()

# 7. Fix the cropping
import matplotlib.pyplot as plt
plt.bar(df_sorted['Team'], df_sorted['Titles'], color='red')
plt.xlabel('Team')
plt.ylabel('Number of Championships')
plt.xticks(rotation=45)
plt.title(title)
plt.savefig('Titles_by_Team.jpeg', bbox_inches='tight') # fix the cropping issue
plt.show()

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

###############################################################################

# Activity 3: Multiple Plot Types using Subplots 

# 1. For line, Bar, and Horizontal Bar plots
# Create a list of strings for x
x = ['Week 1','Week 2','Week 3','Week 4','Week 5']
# Create a list of values for y
y = [300, 200, 400, 350, 500]

# 2. For histogram and Box-and-Whisker
# Create an array of 100 normally distributed numbers
import numpy as np
y2 = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1

# 3. For scatterplot
# Create a list of numbers for x
x2 = [5, 5.5, 5, 5.5, 6, 6.5, 6, 6.5, 7, 5.5, 5.25, 6, 5.25]
# create a list of numbers for y
y3 = [100, 150, 110, 140, 140, 170, 168, 165, 180, 125, 115, 155, 135]

# 4. generate figure
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(x, y)
axes[0,0].set_title('Line Plot')
# Bar plot (top right)
axes[0,1].bar(x, y)
axes[0,1].set_title('Bar Plot')
# Horizontal bar plot (middle left)
axes[1,0].barh(x, y)
axes[1,0].set_title('Horizontal Bar Plot')
# Histogram (middle right)
axes[1,1].hist(y2, bins=20)
axes[1,1].set_title('Histogram')
# Scatterplot (bottom left)
axes[2,0].scatter(x2, y3)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].boxplot(y2)
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

