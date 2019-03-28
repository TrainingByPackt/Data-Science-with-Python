# Exercise 7: Supervised Data Reduction using Linear Discriminant Function Analysis (LDA) 

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

# instantiate model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()

# fit model to X and y
model.fit(X, y)

# get the explained variance ratio
model.explained_variance_ratio_

# transform the features to the components
df_lda = model.transform(X)

# get the number of components
print('The maximum number of components is {}'.format(df_lda.shape[1]))

# split data into testing and training
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_lda, y, test_size=0.33, random_state=42)

# create a random forest model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

# fit the model
model.fit(X_train, y_train)

# generate predictions
predictions = model.predict(X_test)
print(predictions)

# generate confusion matrix
from sklearn.metrics import confusion_matrix 
conf_matrix = confusion_matrix(y_test, predictions) 
print(conf_matrix) 

# style the confusion matrix
import pandas as pd
cm = pd.DataFrame(conf_matrix)
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



