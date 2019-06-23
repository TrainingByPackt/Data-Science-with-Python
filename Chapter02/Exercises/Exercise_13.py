# Exercise 13: Programmatically extracting tuned hyperparameters and determining feature importance from random forest regressor grid search model

# continuing from Activity 6

# instantiate model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(criterion=best_parameters['criterion'],
                              max_features=best_parameters['max_features'],
                              min_impurity_decrease=best_parameters['min_impurity_decrease'],
                              bootstrap=best_parameters['bootstrap'],
                              warm_start=best_parameters['warm_start'])

# fit model
model.fit(X_train_scaled, y_train)

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





