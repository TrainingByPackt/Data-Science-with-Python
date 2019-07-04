# Exercise 6: Scatterplot

# generate list of numbers for height
y = [5, 5.5, 5, 5.5, 6, 6.5, 6, 6.5, 7, 5.5, 5.25, 6, 5.25]
print(y)

# create a list of numbers for weight
x = [100, 150, 110, 140, 140, 170, 168, 165, 180, 125, 115, 155, 135]
print(x)

# create histogram
import matplotlib.pyplot as plt
plt.scatter(x, y) # generate scatterplot
plt.xlabel('Weight') # label x-axis
plt.ylabel('Height') # label y-axis
plt.show() # print plot

# calculate pearson correlations
from scipy.stats import pearsonr
correlation_coeff, p_value = pearsonr(x, y)
print(correlation_coeff)

# Set up some logic
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
print(title)

# Use title as title
import matplotlib.pyplot as plt
plt.scatter(x, y) # generate scatterplot
plt.xlabel('Weight') # label x-axis
plt.ylabel('Height') # label y-axis
plt.title(title) # set programmatic title
plt.show() # print plot
