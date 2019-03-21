# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:11:41 2019

@author: aengland
"""

# data visualizations

# functional method

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

# Activity 3: Multiple Plot Types using Subplots 

# 1. For line, Bar, and Horizontal Bar plots
# import Items_Sold_by_Week.csv
import pandas as pd
Items_by_Week = pd.read_csv('Items_Sold_by_Week.csv')

# 2. For histogram and Box-and-Whisker
# Create an array of 100 normally distributed numbers
import numpy as np
y = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1

# 3. For scatterplot
# import Height_by_Weight.csv
import pandas as pd
Weight_by_Height = pd.read_csv('Weight_by_Height.csv')

# 4. generate figure
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)

# 5. Make sure the plots don't overlap
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
plt.tight_layout() # prevent plot overlap

# 6. Name the titles
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].set_title('Histogram')
# Scatterplot (bottom left)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 7. Line plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].set_title('Histogram')
# Scatterplot (bottom left)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 8. Bar plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].set_title('Histogram')
# Scatterplot (bottom left)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 9. Horizontal bar
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].set_title('Histogram')
# Scatterplot (bottom left)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 10. Histogram
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20)
axes[1,1].set_title('Histogram') # for histogram
# Scatterplot (bottom left)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 11. Histogram
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20)
axes[1,1].set_title('Histogram') # for histogram
# Scatterplot (bottom left)
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 12. Scatterplot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20)
axes[1,1].set_title('Histogram') # for histogram
# Scatterplot (bottom left)
axes[2,0].scatter(Weight_by_Height['Height'], Weight_by_Height['Weight']) # for scatterplot
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 13. Box-and-Whisker
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20) # for histogram
axes[1,1].set_title('Histogram') 
# Scatterplot (bottom left)
axes[2,0].scatter(Weight_by_Height['Height'], Weight_by_Height['Weight']) # for scatterplot
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].boxplot(y) # for Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 14. Set x- and y-axis for each subplot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_xlabel('Week')
axes[0,0].set_ylabel('Items Sold')
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_xlabel('Week')
axes[0,1].set_ylabel('Items Sold')
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_xlabel('Items Sold')
axes[1,0].set_ylabel('Week')
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20) # for histogram
axes[1,1].set_xlabel('y')
axes[1,1].set_ylabel('Frequency')
axes[1,1].set_title('Histogram') 
# Scatterplot (bottom left)
axes[2,0].scatter(Weight_by_Height['Height'], Weight_by_Height['Weight']) # for scatterplot
axes[2,0].set_xlabel('Height')
axes[2,0].set_ylabel('Weight')
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].boxplot(y) # for Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap


# 15. Enlarge the figure size
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(8,8)) # for figure size
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_xlabel('Week')
axes[0,0].set_ylabel('Items Sold')
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_xlabel('Week')
axes[0,1].set_ylabel('Items Sold')
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_xlabel('Items Sold')
axes[1,0].set_ylabel('Week')
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20) # for histogram
axes[1,1].set_xlabel('y')
axes[1,1].set_ylabel('Frequency')
axes[1,1].set_title('Histogram') 
# Scatterplot (bottom left)
axes[2,0].scatter(Weight_by_Height['Height'], Weight_by_Height['Weight']) # for scatterplot
axes[2,0].set_xlabel('Height')
axes[2,0].set_ylabel('Weight')
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].boxplot(y) # for Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap

# 16. Save the figure
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(8,8)) # for figure size
# line plot (top left)
axes[0,0].plot(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for line plot
axes[0,0].set_xlabel('Week')
axes[0,0].set_ylabel('Items Sold')
axes[0,0].set_title('Line')
# Bar plot (top right)
axes[0,1].bar(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for bar plot
axes[0,1].set_xlabel('Week')
axes[0,1].set_ylabel('Items Sold')
axes[0,1].set_title('Bar')
# Horizontal bar plot (middle left)
axes[1,0].barh(Items_by_Week['Week'], Items_by_Week['Items_Sold']) # for horizontal bar plot
axes[1,0].set_xlabel('Items Sold')
axes[1,0].set_ylabel('Week')
axes[1,0].set_title('Horizontal Bar')
# Histogram (middle right)
axes[1,1].hist(y, bins=20) # for histogram
axes[1,1].set_xlabel('y')
axes[1,1].set_ylabel('Frequency')
axes[1,1].set_title('Histogram') 
# Scatterplot (bottom left)
axes[2,0].scatter(Weight_by_Height['Height'], Weight_by_Height['Weight']) # for scatterplot
axes[2,0].set_xlabel('Height')
axes[2,0].set_ylabel('Weight')
axes[2,0].set_title('Scatter')
# Box-and-Whisker
axes[2,1].boxplot(y) # for Box-and-Whisker
axes[2,1].set_title('Box-and-Whisker')
plt.tight_layout() # prevent plot overlap
fig.savefig('Six_Subplots.jpeg') # save figure

