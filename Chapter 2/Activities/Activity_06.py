# Activity 6: Scaling features and tuning a random forest regressor in a pipeline

# continuing from Exercise 12

# Set up the steps for a pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
steps = [('scaler', StandardScaler()), ('Forest', RandomForestRegressor(n_estimators=10))] 

# Setup the pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline(steps)

# Specify the hyperparameter space
import numpy as np
parameters = {'Forest__criterion': ['mse','mae'],
              'Forest__max_features': ['auto', 'sqrt', 'log2', None],
              'Forest__min_impurity_decrease': np.linspace(0.0, 1.0, 10),
              'Forest__bootstrap': [True, False],
              'Forest__warm_start': [True, False]}

# Instantiate the GridSearchCV model
from sklearn.model_selection import GridSearchCV
model = GridSearchCV(pipeline, parameters, scoring='explained_variance', cv=5)

# Fit to the training set
model.fit(X_train, y_train)

# Print the tuned parameters
best_parameters = model.best_params_
print(best_parameters)


