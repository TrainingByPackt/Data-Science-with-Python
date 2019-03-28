# Activity 2: Evaluating mean inertia by cluster after PCA transformation

# not: in order for the bottom plot to properly run, we must have mean_inertia_list_PCA (from Exercise 4) in our environment

# now, we can fit it to the k-means algorithm
from sklearn.decomposition import PCA
model = PCA(n_components=best_n_components) # remember, best_n_components = 6

# fit model
model.fit(scaled_features)

# transform into principal components
df_pca = model.transform(scaled_features)

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