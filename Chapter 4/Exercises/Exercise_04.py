# Exercise 4: Fitting k-Means Model

# import data
import pandas as pd
df = pd.read_csv('glass.csv')

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # create StandardScaler() object
scaled_features = scaler.fit_transform(df_shuffled) # fit scaler model and transform df_shuffled

# instantiate kmeans model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=2)

# fit model
model.fit(scaled_features)

