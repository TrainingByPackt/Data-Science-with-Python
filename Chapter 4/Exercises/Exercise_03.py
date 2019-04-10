# Exercise 3: Assigning Predicted Clusters to Observations

# get labels
from scipy.cluster.hierarchy import fcluster 
labels = fcluster(model, t=9, criterion='distance')
print(labels)

# assign labels array as a column in df_shuffled
df_shuffled['Predicted_Cluster'] = labels

