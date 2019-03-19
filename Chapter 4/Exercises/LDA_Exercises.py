# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:21:21 2019

@author: aengland
"""

# Supervised learning with LDA

# Exercise 7: Fitting LDA model with default hyperparameters

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)
# insert target as target col
df['target'] = iris.target

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# Save the DV as DV
DV = 'target'

# Get X's and y
X = df_shuffled.drop(DV, axis=1)
y = df_shuffled[DV]

# Create train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# instantiate an LDA model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()

# fit model
model.fit(X_train, y_train)

# generate predictions
predictions = model.predict(X_test)
print(predictions)

# evaluate performance using a confusion matrix
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_test, predictions)
print(conf_matrix)

# style the confusion matrix to make less confusing
import pandas as pd
cm = pd.DataFrame(conf_matrix)
import numpy as np
cm['Total'] = np.sum(cm, axis=1)
cm = cm.append(np.sum(cm, axis=0), ignore_index=True)
cm.columns = ['Predicted 0', 'Predicted 1', 'Predicted 2', 'Total']
cm = cm.set_index([['Actual 0', 'Actual 1', 'Actual 2', 'Total']])
print(cm)

###############################################################################

# Exercise 8: Tuning LDA Hyperparameters using GridSearchCV

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the features as df
import pandas as pd
df = pd.DataFrame(iris.data)
# insert target as target col
df['target'] = iris.target

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# Save the DV as DV
DV = 'target'

# Get X's and y
X = df_shuffled.drop(DV, axis=1)
y = df_shuffled[DV]

# Create train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# instantiate a grid with the possible values for hyperparamters (see documentation)
grid = {'solver': ['lsqr', 'eigen'],
        'shrinkage': [None, 'auto']}
print(grid)

from sklearn.model_selection import GridSearchCV
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = GridSearchCV(LinearDiscriminantAnalysis(), grid, scoring='accuracy', cv=5)

# fit the gridsearch model
model.fit(X_train, y_train)

# get a dictionary for best hyperparamters
best_parameters = model.best_params_
print(best_parameters)

# get predictions
predictions = model.predict(X_test)
print(predictions)

# evaluate performance using a confusion matrix
from sklearn.metrics import confusion_matrix
import numpy as np
cm = pd.DataFrame(confusion_matrix(y_test, predictions))
cm['Total'] = np.sum(cm, axis=1)
cm = cm.append(np.sum(cm, axis=0), ignore_index=True)
cm.columns = ['Predicted 0', 'Predicted 1', 'Predicted 2', 'Total']
cm = cm.set_index([['Actual 0', 'Actual 1', 'Actual 2', 'Total']])
print(cm)

# refit LDA model with tuned parameters
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis(solver=best_parameters['solver'],
                                   shrinkage=best_parameters['shrinkage'])

# fit the model
model.fit(X_train, y_train)
