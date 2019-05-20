#!/usr/bin/env python
# coding: utf-8
# Author : Noordeen
# Date : 22-04-2019

import pandas as pd
from sklearn.preprocessing import LabelEncoder

#reading the data into the dataframe into the object data
df = pd.read_csv('Banking_Marketing.csv', header=0)

#finding the data types of each column
print("dtypes:",df.dtypes)

#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print("info:",info)

#Filtering just the categorical variables 
data_column_category = df.select_dtypes(exclude=[np.number]).columns
data_column_category
#performing Dummy variable encoding
for var in data_column_category:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1=df.join(cat_list)
    df=data1

print(df)



