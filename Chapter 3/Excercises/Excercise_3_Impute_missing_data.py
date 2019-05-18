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

#Filling the missing values in the column age with mean
mean_age = df.age.mean()
print(mean_age)
df.age.fillna(df.age.mean(),inplace=True)

#imputing the missing values with median
median_duration = df.duration.median()
print(median_duration)
df.duration.fillna(median_duration,inplace=True)

#imputing the missing values with mode
mode_contact = df.contact.mode()[0]
print(mode_contact)
df.contact.fillna(mode_contact,inplace=True)


