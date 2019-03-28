# Exercise 1: Segmenting Flower Species using Hierarchical Cluster Analysis 

# import data
import pandas as pd
df = pd.read_csv('glass.csv')

# explore data dimensions
n_rows = df.shape[0]
n_columns = df.shape[1]
print('There are {} rows and {} columns in the Glass data set'.format(n_rows, n_columns))

# get df info
print(df.info())

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # instantiate sclaer object
scaler.fit(df_shuffled) # fit scaler to the features
scaled_features = scaler.transform(df_shuffled) # transform features to scaled version

# create linkage model
from scipy.cluster.hierarchy import linkage 
model = linkage(scaled_features, method='complete')

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