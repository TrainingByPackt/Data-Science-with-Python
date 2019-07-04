# Exercise 7: Choosing n_components using Threshold

# Continuing from Exercise 6:

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
    
# print the best number of n_components
print('The best n_components is {}'.format(best_n_components))