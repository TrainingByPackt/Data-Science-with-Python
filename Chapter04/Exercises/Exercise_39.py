# Exercise 6: Fitting PCA Model

# import data
import pandas as pd
df = pd.read_csv('glass.csv')

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # instantiate scaler object
scaled_features = scaler.fit_transform(df_shuffled) # fit and transform df_shuffled

# instantiate PCA model
from sklearn.decomposition import PCA
model = PCA()

# fit model
model.fit(scaled_features)

# get proportion of explained variance in each component
explained_var_ratio = model.explained_variance_ratio_

# print the explained variance ratio
print(explained_var_ratio)
