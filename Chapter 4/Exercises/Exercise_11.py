# Exercise 11: Tuning LDA n_components

# import dependencies
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

accuracy_list = [] # instantiate an empty list for which to append accuracy scores
for i in range(2):
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
