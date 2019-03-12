# Unsupervised Learning

# Part B - Hierarchical clustering

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


###############################################################################
# end of analysis
# continue for scaling formulas
###############################################################################

# to calculate min-max normalization

# create a list of numbers
list_of_numbers = [3,5,4,7,4,3]
# calculate the minimum of the list
minimum_of_list = min(list_of_numbers)
# calculate the maximum of the list
maximum_of_list = max(list_of_numbers)
# instantiate an empty list to append the normalized numbers
min_max_normed_list = []
# iterate through each item in the list of numbers
for i in range(len(list_of_numbers)):
    # calculate the numerator
    numerator = list_of_numbers[i] - minimum_of_list
    # calculate the denominator
    denominator = maximum_of_list - minimum_of_list
    # calculate the normalized score
    min_max_normed = numerator/denominator
    # append this score to the empty list
    min_max_normed_list.append(min_max_normed)
print(min_max_normed_list)
    

# create a list of numbers
list_of_numbers = [3,5,4,7,4,3]

# define a min-max norm function
def Min_Max_Norm(list_of_numbers):
    # calculate the minimum of the list
    minimum_of_list = min(list_of_numbers)
    # calculate the maximum of the list
    maximum_of_list = max(list_of_numbers)
    # instantiate an empty list to append the normalized numbers
    min_max_normed_list = []
    # iterate through each item in the list of numbers
    for i in range(len(list_of_numbers)):
        # calculate the numerator
        numerator = list_of_numbers[i] - minimum_of_list
        # calculate the denominator
        denominator = maximum_of_list - minimum_of_list
        # calculate the normalized score
        min_max_normed = numerator/denominator
        # append this score to the empty list
        min_max_normed_list.append(min_max_normed)
    return min_max_normed_list

# test the function on the   
normalized_values = Min_Max_Norm(list_of_numbers)
print(normalized_values)

###############################################################################

# to calculate z-score

# create a list of numbers
list_of_numbers = [3,5,4,7,4,3]

# get mean
mean_of_list = sum(list_of_numbers)/len(list_of_numbers)
# get standard deviation
import numpy as np
standard_dev = np.std(list_of_numbers)
# get z scores
z_score_list = []
for i in range(len(list_of_numbers)):
	z_score = (list_of_numbers[i] - mean_of_list)/standard_dev
	z_score_list.append(z_score)
# return the z score list
print(z_score_list)



# define a z-score conversion user-defined function
import numpy as np

list_of_numbers = [3,5,4,7,4,3]

def Z_Score_Convert(list_of_numbers):
	# get mean
	mean_of_list = sum(list_of_numbers)/len(list_of_numbers)
	# get standard deviation
	standard_dev = np.std(list_of_numbers)
	# get z scores
	z_score_list = []
	for i in range(len(list_of_numbers)):
		z_score = (i - mean_of_list)/standard_dev
		z_score_list.append(z_score)
	# return the z score list
	return z_score_list

# test the function on the   
normalized_values = Z_Score_Convert(list_of_numbers)
print(normalized_values)



