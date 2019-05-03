# Exercise 11: Programmatically extracting tuned hyperparameters from decision tree classifier grid search model

# continuing from Exercise 10:

# print best_paramters dictionary
print(best_parameters)

# access the 'Tree__criterion' value
print(best_parameters['Tree__criterion'])

# instantiate model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(class_weight=best_parameters['Tree__class_weight'],
                               criterion=best_parameters['Tree__criterion'],
                               min_impurity_decrease=best_parameters['Tree__min_impurity_decrease'],
                               min_weight_fraction_leaf=best_parameters['Tree__min_weight_fraction_leaf'],
                               presort=best_parameters['Tree__presort'])

# fit model
model.fit(X_train, y_train)

# extract feature_importances attribute
print(model.feature_importances_)

# plot feature importance in descending order
import pandas as pd
import matplotlib.pyplot as plt
df_imp = pd.DataFrame({'Importance': list(model.feature_importances_)}, index=X.columns)
# sort dataframe
df_imp_sorted = df_imp.sort_values(by=('Importance'), ascending=True)
# plot these
df_imp_sorted.plot.barh(figsize=(5,5))
plt.title('Relative Feature Importance')
plt.xlabel('Relative Importance')
plt.ylabel('Variable')
plt.legend(loc=4)
plt.show()






