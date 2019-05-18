import pandas as pd 
#reading the data into the dataframe into the object data
df = pd.read_csv("USA_Housing.csv", header=0)
print("df.head() : \n",df.head())
print("df.shape : ",df.shape)
print("df.columns : ",df.columns)
print("df.index : ",df.index)
df.set_index('Address', inplace=True)
print("df.head() after making Adress column as index: \n",df.head())
df.reset_index(inplace=True)
print("df.head() after reseting back to original dataframe: \n",df.head())
df.iloc[0:4,0:3]
df.loc[0:4,["Avg. Area Income", "Avg. Area House Age"]]
X = df.drop('Price', axis=1)
y = df['Price']
print("y.head(10) : \n",y.head(10))
print("y.shape : ",y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print("X_train : ",X_train.shape)
print("X_test : ",X_test.shape)
print("y_train : ",y_train.shape)
print("y_test : ",y_test.shape)