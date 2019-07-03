# Exercise 1: Preparing data for linear regression model

# import data
import pandas as pd
df = pd.read_csv('weather.csv')

# check info
df.info() 

# get number of levels in 'Summary'
levels = len(pd.value_counts(df['Description']))
print('There are {} levels in the Description column'.format(levels))

# dummy code 'Summary'
import pandas as pd
df_dummies = pd.get_dummies(df, drop_first=True)

# check info
print('There are {} columns in df_dummies'.format(df_dummies.shape[1]))

# shuffle df_dummies
from sklearn.utils import shuffle
df_shuffled = shuffle(df_dummies, random_state=42)

# split df_shuffled into X and y
DV = 'Temperature_c' # Save the DV as DV
X = df_shuffled.drop(DV, axis=1) # get features (X)
y = df_shuffled[DV] # get DV (y)

# split X and y into testing and training data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)