# Exercise 8: Tuning LDA Hyperparameters using GridSearchCV

# import data
import pandas as pd
df = pd.read_csv('glass_w_outcome.csv')

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() # create StandardScaler() object
scaler.fit(df_shuffled) # fit scaler to the features
scaled_features = scaler.transform(df_shuffled) # transform features to scaled version

# Save the DV as DV
DV = 'Type'

# Get X's and y
X = df_shuffled.drop(DV, axis=1)
y = df_shuffled[DV]

# Create train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# instantiate a grid with the possible values for hyperparamters (see documentation)
import numpy as np
grid = {'solver': ['lsqr', 'eigen'],
        'shrinkage': [None, 'auto']}
print(grid)

# instantiate gridsearch model
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
import pandas as pd
cm = pd.DataFrame(confusion_matrix(y_test, predictions))
import numpy as np
cm['Total'] = np.sum(cm, axis=1)
cm = cm.append(np.sum(cm, axis=0), ignore_index=True)
cm.columns = ['Predicted 1', 'Predicted 2', 'Predicted 3', 'Total']
cm = cm.set_index([['Actual 1', 'Actual 2', 'Actual 3', 'Total']])
print(cm)

# if we want a classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, predictions))

# to get the accuracy score
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

# refit LDA model with tuned parameters
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis(solver=best_parameters['solver'],
                                   shrinkage=best_parameters['shrinkage'])

# fit the model
model.fit(X_train, y_train)








