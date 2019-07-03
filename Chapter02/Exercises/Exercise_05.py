# Exercise 5: Box-and-Whisker plot

# Generate a list of normally distributed numbers
import numpy as np
y = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1

# Generate boxplot
import matplotlib.pyplot as plt # import matplotlib
plt.boxplot(y) # create boxplot of y
plt.show() # print plot

# Calculate shapiro wilk p-value
from scipy.stats import shapiro
shap_w, shap_p = shapiro(y)
print(shap_p)

# Get outliers
# convert to z-scores
from scipy.stats import zscore
y_z_scores = zscore(y) # convert y into z scores

# get the number of scores with absolute value of 3 or more
total_outliers = 0
for i in range(len(y_z_scores)):
    if abs(y_z_scores[i]) >= 3:
        total_outliers += 1
print(total_outliers)
           
# set up some logic for the title
if shap_p > 0.05:
    title = 'Normally distributed with {} outlier(s).'.format(total_outliers)
else:
    title = 'Not normally distributed with {} outlier(s).'.format(total_outliers)
print(title)

# Generate boxplot with programmatic tile
import matplotlib.pyplot as plt # import matplotlib
plt.boxplot(y) # generate boxplot
plt.title(title) # programmatic title
plt.show() # print plot