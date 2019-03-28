# Activity 1: K-Means Clustering (ensemble) 

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

# instantiate an empty dataframe
import pandas as pd
labels_df = pd.DataFrame()

# Build 100 models
from sklearn.cluster import KMeans
for i in range(1, 101):
    model = KMeans(n_clusters=2)
    model.fit(scaled_features) # fit model
    labels = model.labels_ # get predicted labels
    labels_df['Model_{}_Labels'.format(i)] = labels # put the labels into the empty df
print('There are {} rows and {} columns in the labels_df data frame'.format(labels_df.shape[0], labels_df.shape[1]))

# now, we will get predictions across columns
labels_df['row_mode'] = labels_df.mode(axis=1)

# check out the frequency of each cluster
import pandas as pd
pd.value_counts(labels_df['row_mode'])