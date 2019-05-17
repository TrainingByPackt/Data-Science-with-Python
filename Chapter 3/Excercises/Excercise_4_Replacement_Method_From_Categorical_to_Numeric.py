#!/usr/bin/env python
# coding: utf-8
# Author : Noordeen
# Date : 22-04-2019
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("student.csv")

df.shape

df_categorical = df.select_dtypes(exclude=np.number)

df_categorical

df_categorical.Grade.value_counts()

df_categorical.Gender.value_counts()

df_categorical.Employed.value_counts()

df_categorical.Grade.replace({"1st Class":3, "2nd Class":2, "3rd Class":1}, inplace= True)

df_categorical.Employed.replace({"yes":1,"no":0}, inplace = True)

df_categorical.Gender.replace({"Male":0,"Female":1}, inplace = True)

print(df_categorical.head())



