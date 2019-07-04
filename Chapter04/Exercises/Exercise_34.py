# Exercise 1: Building HCA Model 

# import data
import pandas as pd
df = pd.read_csv('glass.csv')

# get df info
print(df.info())

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # instantiate scaler object
scaled_features = scaler.fit_transform(df_shuffled) # fit and transform df_shuffled

# create linkage model
from scipy.cluster.hierarchy import linkage 
model = linkage(scaled_features, method='complete')



