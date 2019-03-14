# Unsupervised Learning

# Exercise 1: Segmenting Flower Species using Hierarchical Cluster Analysis 

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the data as df
import pandas as pd
df = pd.DataFrame(iris.data)

# explore data dimensions
n_rows = df.shape[0]
n_columns = df.shape[1]
print('There are {} rows and {} columns in the Iris data set'.format(n_rows, n_columns))

# get df info
print(df.info())

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

#################### BRIEF SCALING INTERMITION ################################

# min-max normalization
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# calculate the denominator
denominator = maximum_of_list - minimum_of_list
# calculate the numerator
numerator = list_of_numbers[0] - minimum_of_list
# calculate the min-max normed value
min_max_normed_value = numerator/denominator
print(min_max_normed_value)


# min-max normalization loop
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# calculate the denominator
denominator = maximum_of_list - minimum_of_list
# instantiate an empty list for which to append
min_maxed_list_of_numbers = []
for i in range(len(list_of_numbers)): 
    # calculate the numerator
    numerator = list_of_numbers[i] - minimum_of_list
    # calculate the min-max normed value
    min_max_normed_value = numerator/denominator
    # append the min max normed value to the empty list
    min_maxed_list_of_numbers.append(min_max_normed_value)
print(min_maxed_list_of_numbers)

###############################################################################

# min-max normalization
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# calculate the denominator
denominator = maximum_of_list - minimum_of_list
# calculate the numerator
numerator = list_of_numbers[0] - minimum_of_list
# calculate the min-max normed value
min_max_normed_value = numerator/denominator
print(min_max_normed_value)


# min-max normalization loop
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# calculate the denominator
denominator = maximum_of_list - minimum_of_list
# instantiate an empty list for which to append
min_maxed_list_of_numbers = []
for i in range(len(list_of_numbers)): 
    # calculate the numerator
    numerator = list_of_numbers[i] - minimum_of_list
    # calculate the min-max normed value
    min_max_normed_value = numerator/denominator
    # append the min max normed value to the empty list
    min_maxed_list_of_numbers.append(min_max_normed_value)
print(min_maxed_list_of_numbers)

###############################################################################

# Activity 1: Calculating a Z-score
list_of_numbers = [3,5,4,7,4,3]
# get mean
import numpy as np
mean_of_list = np.mean(list_of_numbers)
# get denominator (i.e., sd)
denominator = np.std(list_of_numbers)
# get numerator
numerator = list_of_numbers[0] - mean_of_list
# calculate z score
z_score = numerator/denominator
print(z_score)


# Activity 2: Convert a List of Values to Z-Scores
list_of_numbers = [3,5,4,7,4,3]
# get mean
import numpy as np
mean_of_list = np.mean(list_of_numbers)
# get denominator (i.e., sd)
denominator = np.std(list_of_numbers)
# instantiate empty list for which to append z-scores
z_score_list = []
for i in range(len(list_of_numbers)):
    # get numerator
    numerator = list_of_numbers[i] - mean_of_list
    # calculate z score
    z_score = numerator/denominator
    # append z score to z_score_list
    z_score_list.append(z_score)
print(z_score_list)

###############################################################################

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# create linkage model
from scipy.cluster.hierarchy import linkage 
model = linkage(scaled_features, method='complete') 

# plot dendrogram
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram
plt.figure(figsize=(10,5))
plt.title('Dendrogram')
dendrogram(model,
           leaf_rotation=90,
           leaf_font_size=6)
plt.show()

# get labels
from scipy.cluster.hierarchy import fcluster 
labels = fcluster(model, t=5, criterion='distance') # don't merge clusters further aprt than 5 (see dendrogram)
print(labels)

# assign labels array as a column in df_shuffled
df_shuffled['Predicted_Cluster'] = labels



