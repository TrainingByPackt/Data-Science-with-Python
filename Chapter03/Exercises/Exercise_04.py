# Exercise 4: Fitting a multiple linear regression model and determining the intercept and coefficient

# continuing from Exercise 3:

# instantiate linear regression model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# fit model to training data
model.fit(X_train, y_train)

# extract the intercept
intercept = model.intercept_

# extract the coefficients
coefficients = model.coef_

# print the formula
print('Temperature = {0:0.2f} + ({1:0.2f} x Humidity) + ({2:0.2f} x Wind Speed) + ({3:0.2f} x Wind Bearing Degrees) + ({4:0.2f} x Visibility) + ({5:0.2f} x Pressure) + ({6:0.2f} x Rain) + ({7:0.2f} x Normal Weather) + ({8:0.2f} x Warm Weather)'.format(intercept, 
                                                                                                                                                                                                                                                            coefficients[0],
                                                                                                                                                                                                                                                            coefficients[1],
                                                                                                                                                                                                                                                            coefficients[2],
                                                                                                                                                                                                                                                            coefficients[3],
                                                                                                                                                                                                                                                            coefficients[4],
                                                                                                                                                                                                                                                            coefficients[5],
                                                                                                                                                                                                                                                            coefficients[6],
                                                                                                                                                                                                                                                            coefficients[7]))

 
                                                                  