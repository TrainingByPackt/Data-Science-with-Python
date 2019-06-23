# Activity 6: Tuning a random forest regressor

# continuing from Exercise 12

# Specify the hyperparameter space
import numpy as np
grid = {'criterion': ['mse','mae'],
        'max_features': ['auto', 'sqrt', 'log2', None],
        'min_impurity_decrease': np.linspace(0.0, 1.0, 10),
        'bootstrap': [True, False],
        'warm_start': [True, False]}

# Instantiate the GridSearchCV model
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
model = GridSearchCV(RandomForestRegressor(), grid, scoring='explained_variance', cv=5)

# Fit to the training set
model.fit(X_train_scaled, y_train)

# Print the tuned parameters
best_parameters = model.best_params_
print(best_parameters)


