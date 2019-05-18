#!/usr/bin/env python
# coding: utf-8
# Author : Noordeen
# Date : 22-04-2019

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#reading the data into the dataframe into the object data
df = pd.read_csv('Banking_Marketing.csv'', header=0)

#finding the data types of each column
print("dtypes:",df.dtypes)

#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print("info:",info)

#Dropping Missing Values
df = df.dropna()

#Filtering the categorical variabels
#cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
data_column_category = df.select_dtypes(exclude=[np.number]).columns

#performing label encoding
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])
print("Label Encoded Data: ")
print(df)


