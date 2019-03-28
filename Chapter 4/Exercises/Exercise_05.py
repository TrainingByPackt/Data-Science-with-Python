# Exercise 5: Principal Component Analysis (PCA) with 2 Principal Components

from sklearn.decomposition import PCA
model = PCA(n_components=2) # instantiate pca model

# fit model
model.fit(scaled_features)

# get explained variance ratio
explained_var_ratio = model.explained_variance_ratio_
print(explained_var_ratio)

# get the total explained variance with these 2 components
print('The total percentage of explained variance for the first 2 principal components is {0:0.2f}%'.format(sum(explained_var_ratio)*100))

# transform X into X_pca
df_pca = model.transform(scaled_features)

"""
Without clearing the kernel, continue to exercise 6. 
We do not want to clear the kernel because we need to keep mean_inertia_list
in our environment, so we can plot inertia by n_clusters for original features
and PCA transformed features in the same plot
"""