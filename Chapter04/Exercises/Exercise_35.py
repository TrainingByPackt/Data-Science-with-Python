# Exercise 2: Plotting HCA Model and Assigning Predictions

# continuing from exercise 1:

# plot dendrogram
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram
plt.figure(figsize=(10,5))
plt.title('Dendrogram for Glass Data')
dendrogram(model,
           leaf_rotation=90,
           leaf_font_size=6)
plt.show()

# get labels
from scipy.cluster.hierarchy import fcluster 
labels = fcluster(model, t=9, criterion='distance')
print(labels)

# assign labels array as a column in df_shuffled
df_shuffled['Predicted_Cluster'] = labels

# preview data
print(df_shuffled.head(5))