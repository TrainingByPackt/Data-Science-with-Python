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
import numpy as np
cm = pd.DataFrame(confusion_matrix(y_test, predictions))
cm['Total'] = np.sum(cm, axis=1)
cm = cm.append(np.sum(cm, axis=0), ignore_index=True)
cm.columns = ['Predicted 0', 'Predicted 1', 'Predicted 2', 'Total']
cm = cm.set_index([['Actual 0', 'Actual 1', 'Actual 2', 'Total']])
print(cm)

###############################################################################

# Activity 3: Tuning LDA Hyperparameters using GridSearchCV

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

###############################################################################

# Exercise 8: Tuning LDA Hyperparameters in a Pipeline

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

# Save the DV as DV
DV = 'target'

# Get X's and y
X = df_shuffled.drop(DV, axis=1)
y = df_shuffled[DV]

# Create train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# now, we will scale, tune, and fit our model using a pipeline

# Set up the steps for a pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
steps = [('scaler', StandardScaler()), ('LDA', LinearDiscriminantAnalysis())] 

# Setup the pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'LDA__solver': ['lsqr', 'eigen'],
              'LDA__shrinkage': [None, 'auto']}

# Instantiate the GridSearchCV model
from sklearn.model_selection import GridSearchCV
model = GridSearchCV(pipeline, parameters, scoring='accuracy', cv=5)

# fit the gridsearch model
model.fit(X_train, y_train)

# get a dictionary for best hyperparamters
best_parameters = model.best_params_
print(best_parameters)

# instantiate LDA model with these paramters
model = LinearDiscriminantAnalysis(solver=best_parameters['LDA__solver'],
                                   shrinkage=best_parameters['LDA__shrinkage'])

# fit the model
model.fit(X_train, y_train)

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

# evaluate model performance using a classification report
from sklearn.metrics import classification_report
cr = classification_report(y_test, predictions)
print(cr)





model.coef_ 

model.intercept_ 

model.covariance_ 

model.means_ 

model.priors_ 

model.classes_ 