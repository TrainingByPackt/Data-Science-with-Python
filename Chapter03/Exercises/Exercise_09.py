# Exercise 9: Fitting LDA Model

# import data
import pandas as pd
df = pd.read_csv('glass_w_outcome.csv')

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# Save the DV as DV
DV = 'Type'

# Get X's and y
X = df_shuffled.drop(DV, axis=1)
y = df_shuffled[DV]

# split into testing and training before transforming into its components
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# standardize X_train and X_test
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # create StandardScaler() object
X_train_scaled = scaler.fit_transform(X_train) # fit scaler model and transform X_train
X_test_scaled = scaler.transform(X_test) # transform X_test

# instantiate LDA model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()

# fit the model on the training data
model.fit(X_train_scaled, y_train)

# compute explained ratio by component
model.explained_variance_ratio_