# Exercise 9: Tuning support vector classifier using grid search

# continuing from exercise 8:

# instantiate grid
import numpy as np
grid = {'C': np.linspace(1, 10, 10),
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'shrinking': [True, False],
        'tol': np.linspace(0.001, 1, 10)}

# instantiate GridSearchCV model
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
model = GridSearchCV(SVC(gamma='auto', probability=True), grid, scoring='f1', cv=5)

# fit the gridsearch model
model.fit(X_train, y_train)

# print the best parameters
best_parameters = model.best_params_
print(best_parameters)