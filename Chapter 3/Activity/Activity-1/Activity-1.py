#!/usr/bin/env python
# coding: utf-8
# Author : Mohamed Noordeen
# Date : 22-04-2019


#import Library
import pandas as pd


# 1.Load the Data


df = pd.read_csv("Wholesale customers data.csv")


# 2.Understand the Data Features



#Finding number of rows and columns
print("Number of rows and columns : ",df.shape)



#Basic Information about all the columns
print("Basic Information about all the column : ")
print(df.info())



#Basic Statistics about all the columns
print("Basic Statistics about all the column : ")
print(df.describe().transpose())


# 3.Check for NULL values and their datatypes



#checking for any null in each column
null_ = df.isna().any()
print(null_)



#findind datatypes of each column
dtypes = df.dtypes
print(dtypes)



#Combining both null and datatypes of each column
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print(info)


# 4.Remove the missing values (if any)
# 
# Since there are no missing values in the data set we have nothing to handle



#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
info = pd.concat([null_,dtypes],axis = 1,keys = ['Null','type'])
print(info)


# 5.Perform Feature Scaling

from sklearn import preprocessing
 
std_scale = preprocessing.StandardScaler().fit(df)
df_std = pd.DataFrame(std_scale.transform(df),columns=df.columns)
print("Standardised data : \n",df_std)

