# Exercise 8: LDA: Tuning n_components

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

# split into testing and training before transforming into its components
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# find the maximum value of n_components:
# 1. instantiate model
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()

# 2. fit model to X and y
model.fit(X_train, y_train)

# 3. get the length of the explained variance ratio because that list will have an item for each component
max_n_components = len(model.explained_variance_ratio_)
print(max_n_components)

# import dependencies
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

accuracy_list = [] # instantiate an empty list for which to append accuracy scores
for i in range(max_n_components):
    model = LinearDiscriminantAnalysis(n_components=i+1) # instantiate model
    model.fit(X_train, y_train) # fit model to training data
    X_train_LDA = model.transform(X_train) # transform the training features to the training components
    X_test_LDA = model.transform(X_test) # transform the testing features to the testing components
    model = RandomForestClassifier() # create a random forest model
    model.fit(X_train_LDA, y_train) # fit the model on the training components
    predictions = model.predict(X_test_LDA) # generate predictions on the testing components
    accuracy = accuracy_score(y_test, predictions) # get the accuracy score
    accuracy_list.append(accuracy) # append accuracy score to accuracy_list
print(accuracy_list)

# find the maximum of accuracy_list
max_accuracy = max(accuracy_list)
print(max_accuracy)

# find the index of the maximum value in the list
index_max_accuracy = accuracy_list.index(max_accuracy)
print(index_max_accuracy)

# Print off which number of n_components is best and what the accuracy percent is
print('{0} component(s) are used to achieve {1:0.2f}% accuracy'.format(index_max_accuracy+1, max_accuracy*100))

