# Exercise 2: Segmenting Iris into 2 Clusters using k-Means 

# import data
import pandas as pd
df = pd.read_csv('glass.csv')

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # create StandardScaler() object
scaler.fit(df_shuffled) # fit scaler to the features
scaled_features = scaler.transform(df_shuffled) # transform features to scaled version

# instantiate kmeans model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=2)

# fit model
model.fit(scaled_features)

# get the cluster centroids
centroids = model.cluster_centers_ 
print(centroids)

# get the inertia
inertia = model.inertia_ 
print('The within-group sum of squares (i.e., inertia) with 2 clusters is {0:0.2f}'.format(inertia))

# get predicted labels
labels = model.labels_
print(labels)

# see how many of each label we have
import pandas as pd
pd.value_counts(labels)

# add label to df_shuffled
df_shuffled['Predicted_Cluster'] = labels
print(df_shuffled.head(5))