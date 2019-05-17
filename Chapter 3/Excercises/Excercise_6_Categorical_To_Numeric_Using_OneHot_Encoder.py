#!/usr/bin/env python
# coding: utf-8
# Author : Noordeen
# Date : 22-04-2019

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#reading the data into the dataframe into the object data
df = pd.read_csv('Banking_Marketing.csv', header=0)

#finding the data types of each column
print("dtypes:",df.dtypes)

#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print("info:",info)

#Filtering the categorical variabels
data_column_category = df.select_dtypes(exclude=[np.number]).columns
data_column_category

#performing label encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])
    
#Performing Onehot Encoding
onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoded = onehot_encoder.fit_transform(df[data_column_category])
onehot_encoded = pd.DataFrame(onehot_encoded,columns = onehot_encoder.get_feature_names(data_column_category))
print(onehot_encoded)


