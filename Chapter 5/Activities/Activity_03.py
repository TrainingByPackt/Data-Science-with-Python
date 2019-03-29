# Activity 3: Multiple Plot Types using Subplots 

# For line, Bar, and Horizontal Bar plots
# import Items_Sold_by_Week.csv
import pandas as pd
Items_by_Week = pd.read_csv('Items_Sold_by_Week.csv')

# For histogram and Box-and-Whisker
# Create an array of 100 normally distributed numbers
import numpy as np
y = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1

# For scatterplot
# import Height_by_Weight.csv
import pandas as pd
Weight_by_Height = pd.read_csv('Weight_by_Height.csv')

# generate figure
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
plt.show() 

# Make sure the plots don't overlap
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=3, ncols=2)
plt.tight_layout() # prevent plot overlap
plt.show() 

# Name the titles
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
plt.show() 

# Line plot
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
plt.show() 

# Bar plot
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
plt.show() 

# Horizontal bar
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
plt.show() 

# Histogram
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
plt.show() 

# Scatterplot
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
plt.show() 

# Box-and-Whisker
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
plt.show() 

# Set x- and y-axis for each subplot
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
plt.show() 


# Enlarge the figure size
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
plt.show() 

# Save the figure
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
plt.show() 