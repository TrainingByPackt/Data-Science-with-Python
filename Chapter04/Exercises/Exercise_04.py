# Exercise 4: Calculating Mean Inertia by n_clusters

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

# calculate mean inertia by n_clusters
from sklearn.cluster import KMeans
import numpy as np
mean_inertia_list = [] # create a list for the average inertia at each n_clusters
for x in range(1, 11): # loop through n_clusters 1-10
    inertia_list = [] # create a list for each individual inertia value at n_cluster
    for i in range(100):
        model = KMeans(n_clusters=x) # instantiate model
        model.fit(scaled_features) # fit model
        inertia = model.inertia_ # get inertia
        inertia_list.append(inertia) # append inertia to inertia_list
    # moving to the outside loop
    mean_inertia = np.mean(inertia_list) # get mean of inertia list
    mean_inertia_list.append(mean_inertia) # append mean_inertia to mean_inertia_list
print(mean_inertia_list) 