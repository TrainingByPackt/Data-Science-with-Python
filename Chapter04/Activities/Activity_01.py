# Activity 1: Ensemble k-Means Clustering 

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

# instantiate an empty dataframe
import pandas as pd
labels_df = pd.DataFrame()

# Build 100 models
from sklearn.cluster import KMeans
for i in range(100):
    model = KMeans(n_clusters=2)
    model.fit(scaled_features) # fit model
    labels = model.labels_ # get predicted labels
    labels_df['Model_{}_Labels'.format(i+1)] = labels # put the labels into the empty df

# calculate mode for each row
row_mode = labels_df.mode(axis=1)

# assign the row_mode array as a column in labels_df
labels_df['row_mode'] = row_mode

# preview the data
print(labels_df.head(5))