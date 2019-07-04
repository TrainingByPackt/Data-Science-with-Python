# Exercise 7: Tuning hyperparameters of logistic regression model

# continuing from Exercise 6:

# instantiate a grid with the possible values for hyperparamters (see documentation)
import numpy as np
grid = {'penalty': ['l1', 'l2'],
        'C': np.linspace(1, 10, 10)}

# instantiate GridSearchCV model
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
model = GridSearchCV(LogisticRegression(solver='liblinear'), grid, scoring='f1', cv=5)

# fit the gridsearch model
model.fit(X_train, y_train)

# print the best parameters
best_parameters = model.best_params_
print(best_parameters)

