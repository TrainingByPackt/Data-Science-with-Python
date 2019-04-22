# Exercise 10: Tuning decision tree classifier using grid search in pipeline

# Set up the steps for a pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
steps = [('scaler', StandardScaler()), ('Tree', DecisionTreeClassifier())] 

# Setup the pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline(steps)

# Specify the hyperparameter space
import numpy as np
parameters = {'Tree__criterion': ['gini', 'entropy'],
              'Tree__min_weight_fraction_leaf': np.linspace(0.0, 0.5, 10),
              'Tree__min_impurity_decrease': np.linspace(0.0, 1.0, 10),
              'Tree__class_weight': [None, 'balanced'],
              'Tree__presort': [True, False]}

# Instantiate the GridSearchCV model
from sklearn.model_selection import GridSearchCV
model = GridSearchCV(pipeline, parameters, scoring='f1', cv=5)

# Fit to the training set
model.fit(X_train, y_train)

# Print the tuned parameters
best_parameters = model.best_params_
print(best_parameters)