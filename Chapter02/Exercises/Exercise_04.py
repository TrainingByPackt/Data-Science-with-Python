# Exercise 4: Histogram

# generate list of normally distributed numbers
import numpy as np
y = np.random.normal(loc=0, scale=0.1, size=100) # 100 numbers with mean of 0 and standard deviation of 0.1
print(y)

# create histogram
import matplotlib.pyplot as plt
plt.hist(y, bins=20)
plt.show()

# label the axes
import matplotlib.pyplot as plt
plt.hist(y, bins=20)
plt.xlabel('y Value')
plt.ylabel('Frequency')
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