# Exercise 10: Tuning decision tree classifier using grid search in pipeline

# continuing from Activity 4:

# Specify the hyperparameter space
import numpy as np
grid = {'criterion': ['gini', 'entropy'],
        'min_weight_fraction_leaf': np.linspace(0.0, 0.5, 10),
        'min_impurity_decrease': np.linspace(0.0, 1.0, 10),
        'class_weight': [None, 'balanced'],
        'presort': [True, False]}

# Instantiate the GridSearchCV model
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
model = GridSearchCV(DecisionTreeClassifier(), grid, scoring='f1', cv=5)

# Fit to the training set
model.fit(X_train_scaled, y_train)

# Print the tuned parameters
best_parameters = model.best_params_
print(best_parameters)