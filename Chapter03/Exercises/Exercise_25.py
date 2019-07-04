# Exercise 5: Fitting a logistic regression model and determining the intercept and coefficient

# clear environment prior to running this code

# import data
import pandas as pd
df = pd.read_csv('weather.csv')

# dummy code 'Summary'
import pandas as pd
df_dummies = pd.get_dummies(df, drop_first=True)

# shuffle df_dummies
from sklearn.utils import shuffle
df_shuffled = shuffle(df_dummies, random_state=42)

# split df_shuffled into X and y
DV = 'Rain' # Save the DV as DV
X = df_shuffled.drop(DV, axis=1) # get features (X)
y = df_shuffled[DV] # get DV (y)

# split X and y into testing and training data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42) 

# instantiate logistic regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# fit the model to the training data
model.fit(X_train, y_train)

# extract the intercept
intercept = model.intercept_

# extract the coefficients
coefficients = model.coef_

# place coefficients in a list
coef_list = list(coefficients[0,:])
 
# put coefficients in a df with feature name
coef_df = pd.DataFrame({'Feature': list(X_train.columns),
                        'Coefficient': coef_list})
print(coef_df)



