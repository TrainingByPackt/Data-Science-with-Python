#!/usr/bin/env python
# coding: utf-8
# Author : Noordeen
# Date : 22-04-2019

#Reading Data into the pandas Dataframe
import pandas as pd
df = pd.read_csv("Wholesale customers data.csv")

#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print(info)


#Performng standard scaling
from sklearn import preprocessing
 
minmax_scale = preprocessing.MinMaxScaler().fit(df)
df_minmax = pd.DataFrame(minmax_scale.transform(df),columns = df.columns)
print(df_minmax)

