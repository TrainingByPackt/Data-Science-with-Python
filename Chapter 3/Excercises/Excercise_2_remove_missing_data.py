import pandas as pd

#reading the data into the dataframe into the object data
df = pd.read_csv('Banking_Marketing.csv', header=0)

#finding the data types of each column
print("dtypes:",df.dtypes)

#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print("info:",info)

print("Number of NA's in each column: ",df.isna().sum())

#removing Null values
df = df.dropna()


#Let us check again if NA’s still available
print(df.isna().sum())
