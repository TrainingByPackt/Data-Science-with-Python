# Exercise 2: Fitting a simple linear regression model and determining the intercept and coefficient

# continuing from Exercise 1:

# instantiate linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# fit model to training data
model.fit(X_train[['Humidity']], y_train)

# extract the intercept
intercept = model.intercept_

# extract the coefficient
coefficient = model.coef_

# print the formula
print('Temperature = {0:0.2f} + ({1:0.2f} x Humidity)'.format(intercept, coefficient[0]))
