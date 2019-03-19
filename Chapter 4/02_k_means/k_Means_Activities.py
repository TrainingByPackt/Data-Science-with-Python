# Activity 1: K-Means Clustering (ensemble) 

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# instantiate an empty dataframe
import pandas as pd
labels_df = pd.DataFrame()

# Build 100 models
from sklearn.cluster import KMeans
for i in range(1, 101):
    # k-means ensemble
    model = KMeans(n_clusters=2)
    # fit model
    model.fit(scaled_features)
    # get predicted labels
    labels = model.labels_
    # put the labels into the empty df
    labels_df['Model_{}_Labels'.format(i)] = labels
print('There are {} rows and {} columns in the labels_df data frame'.format(labels_df.shape[0], labels_df.shape[1]))

# now, we will get predictions across columns
labels_df['row_mode'] = labels_df.mode(axis=1)

# check out the frequency of each cluster
import pandas as pd
pd.value_counts(labels_df['row_mode'])

# clear kernel

###############################################################################

# Activity 2: Evaluating mean inertia by cluster after PCA transformation

# not: in order for the bottom plot to properly run, we must have mean_inertia_list_PCA (from Exercise 4) in our environment

# now, we can fit it to the k-means algorithm
from sklearn.decomposition import PCA
model = PCA(n_components=best_n_components) # remember, best_n_components = 2

# fit model
model.fit(scaled_features)

# transform into principal components
df_pca = model.transform(scaled_features)

# fit 100 models for each n_clusters 1-10
from sklearn.cluster import KMeans
import numpy as np
# create a list for the average inertia at each n_clusters
mean_inertia_list_PCA = []
# loop through n_clusters 1-10
for x in range(1, 11):
    # create a list for each individual inertia value at n_cluster
    inertia_list = []
    for i in range(100):
        # instantiate pipeline
        model = KMeans(n_clusters=x)
        # fit pipeline
        model.fit(df_pca)
        # get inertia
        inertia = model.inertia_
        # append inertia to inertia_list
        inertia_list.append(inertia)
    # get mean of inertia list
    mean_inertia = np.mean(inertia_list)
    # append mean_inertia to mean_inertia_list
    mean_inertia_list_PCA.append(mean_inertia)
print(mean_inertia_list_PCA)  
    

# plot inertia by n_clusters with both lines
import matplotlib.pyplot as plt
x = list(range(1,len(mean_inertia_list_PCA)+1))
y = mean_inertia_list_PCA
y2 = mean_inertia_list 
plt.plot(x, y, label='PCA')
plt.plot(x, y2, label='No PCA')
plt.title('Mean Inertia by n_clusters for Original Features and PCA Transformed Features')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.legend()
plt.show()