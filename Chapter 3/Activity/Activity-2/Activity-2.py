#!/usr/bin/env python
# coding: utf-8
#Author: Mohamed Noordeen

#import Library
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ## 1.Load the data set 


df = pd.read_csv("Marketing_subscription_prediction_latest_edited data.csv", header=0)


# ## 2.Feature Overview: Understand the Features well.


#Finding number of rows and columns
print("Number of rows and columns : ",df.shape)


# In[80]:


#Printing all the columns
print(list(df.columns))


#Basic Statistics of each column
df.describe().transpose()


#Basic Information of each column
print(df.info())


# ## 3.Check for NULL values and their data types


#finding the data types of each column and checking for null
#finding the data types of each column and checking for null
null_ = df.isna().any()
dtypes = df.dtypes
sum_na_ = df.isna().sum()
info = pd.concat([null_,sum_na_,dtypes],axis = 1,keys = ['isNullExist','NullSum','type'])
print(info)




# ## 4.Remove the missing values

df = df.dropna()
#Total number of null in each column
print(df.isna().sum())# No NA



## 5. Frequency distribution of Education column
df.education.value_counts()

# ## 6.The education column of the dataset has many categories and we need to reduce the categories for better modelling



#Check for distinct categories in education column
df.education.unique()




#Let us group "basic.4y", "basic.9y" and "basic.6y" together and call them "basic".
df.education.replace({"basic.9y":"Basic","basic.6y":"Basic","basic.4y":"Basic"},inplace=True)



#Check for distinct categories in education column after grouping
df.education.unique()


# ## 6.Select and perform a suitable encoding method for the data



data_column_category = df.select_dtypes(exclude=[np.number]).columns




data_column_category



#Defining a list with all the names of the categorical features in the data
cat_vars=data_column_category
#for every variables in the list getting dummy variable encoded output
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1=df.join(cat_list)
    df=data1


#Categorical features
cat_vars=data_column_category

#All features
data_vars=df.columns.values.tolist()



#neglecting the categorical column for which we have done encoding
to_keep=[i for i in data_vars if i not in cat_vars]
 
#selecting only the numerical and encoded catergorical column
data_final=df[to_keep]



data_final.columns


# ## 7.Split the data into Train and test


#Segregating Independent and Target variable
X=data_final.drop(columns='y')
y=data_final['y']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print("FULL Dateset X Shape: ", X.shape )
print("Train Dateset X Shape: ", X_train.shape )
print("Test Dateset X Shape: ", X_test.shape )


matplotlib.pyplot.show()

