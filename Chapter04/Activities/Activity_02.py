# Activity 2: Evaluating Mean Inertia by Cluster After PCA Transformation

# Continuing from Exercise 7:

from sklearn.decomposition import PCA
model = PCA(n_components=best_n_components) # remember, best_n_components = 6

# fit model and transform scaled_features into best_n_components
df_pca = model.fit_transform(scaled_features)

# fit 100 models for each n_clusters 1-10
from sklearn.cluster import KMeans
import numpy as np
mean_inertia_list_PCA = [] # create a list for the average inertia at each n_clusters
for x in range(1, 11): # loop through n_clusters 1-10
    inertia_list = [] # create a list for each individual inertia value at n_cluster
    for i in range(100):
        model = KMeans(n_clusters=x) # instantiate model
        model.fit(df_pca) # fit model
        inertia = model.inertia_ # get inertia
        inertia_list.append(inertia) # append inertia to inertia_list
    # moving to the outside loop
    mean_inertia = np.mean(inertia_list) # get mean of inertia list
    mean_inertia_list_PCA.append(mean_inertia) # append mean_inertia to mean_inertia_list
    
# print mean_inertia_list_PCA
print(mean_inertia_list_PCA)  