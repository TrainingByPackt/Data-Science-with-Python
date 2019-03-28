# Exerise 6: Principal Component Analysis: Tuning n_components

# instantiate pca model
from sklearn.decomposition import PCA
model = PCA()

# fit model
model.fit(scaled_features)

# transform into principle components
df_pca = model.transform(scaled_features)

# get the cumulative sum of explained variance by each component
import numpy as np
cum_sum_explained_var = np.cumsum(model.explained_variance_ratio_)
print(cum_sum_explained_var)

# set a threshold for % of variance in the data to preserve
threshold = .95
for i in range(len(cum_sum_explained_var)):
    if cum_sum_explained_var[i] >= threshold:
        best_n_components = i+1
        break
    else:
        pass
print('The best n_components is {}'.format(best_n_components))

# plot cumulative explained variance by n_components
import matplotlib.pyplot as plt
x = list(range(1, len(cum_sum_explained_var)+1))
y = cum_sum_explained_var
plt.plot(x, y, color='blue', label='Explained Variance')
plt.title('{0} n_components are suggested to preserve {1} of the variance'.format(best_n_components, threshold))
plt.ylabel('Proportion of Explained Variance')
plt.xlabel('n_components')
plt.xticks(range(1, len(cum_sum_explained_var)+1))
plt.axhline(y=threshold, color='gray', linestyle='--', label = '{} Explained Variance'.format(threshold))
plt.legend(loc='best')
plt.show()

"""
Without clearing the kernel, continue to activity 2. 
We do not want to clear the kernel because we need to keep mean_inertia_list
and best_n_components in our environment, so we can plot inertia by n_clusters 
for original features and PCA transformed features in the same plot
"""