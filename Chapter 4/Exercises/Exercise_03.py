# Exercise 3: K-means clustering: Tuning n_clusters 

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

# get inertia for every cluster
from sklearn.cluster import KMeans
inertia_list = []
for i in range(1, 11):
    model = KMeans(n_clusters=i) # instantiate model
    model.fit(scaled_features) # fit model
    inertia = model.inertia_ # get inertia
    inertia_list.append(inertia) # append inertia to inertia_list
print(inertia_list)
    
# plot inertia by n_clusters
import matplotlib.pyplot as plt
x = list(range(1,11))
y = inertia_list
plt.plot(x, y)
plt.title('Inertia by n_clusters')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.show()

# get the inertia values for 3
print('When n_clusters = 3, inertia = {:0.2f}'.format(y[2]))