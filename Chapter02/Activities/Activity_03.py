# Activity 2: Bar plot

# Create a list for x
x = ['Boston Celtics','Los Angeles Lakers', 'Chicago Bulls', 'Golden State Warriors', 'San Antonio Spurs']
print(x)

# Create a list for y
y = [17, 16, 6, 6, 5]
print(y)

# Put into a data frame so we can sort them
import pandas as pd
df = pd.DataFrame({'Team': x,
                   'Titles': y})

# Sort df by titles
df_sorted = df.sort_values(by=('Titles'), ascending=False)

# Make a programmatic title
team_with_most_titles = df_sorted['Team'][0] # get team with most titles
most_titles = df_sorted['Titles'][0] # get the number of max titles
title = 'The {} have the most titles with {}'.format(team_with_most_titles, most_titles) # create title
print(title)

# Plot it
import matplotlib.pyplot as plt # import matplotlib
plt.bar(df_sorted['Team'], df_sorted['Titles'], color='red') # plot titles by team and make bars red
plt.xlabel('Team') # create x label
plt.ylabel('Number of Championships') # create y label
plt.xticks(rotation=45) # rotate x tick labels 45 degrees
plt.title(title) # title
plt.savefig('Titles_by_Team') # save figure to present working directory
plt.show() # print plot

# Fix the cropping
import matplotlib.pyplot as plt
plt.bar(df_sorted['Team'], df_sorted['Titles'], color='red')
plt.xlabel('Team')
plt.ylabel('Number of Championships')
plt.xticks(rotation=45)
plt.title(title)
plt.savefig('Titles_by_Team', bbox_inches='tight') # fix the cropping issue
plt.show()