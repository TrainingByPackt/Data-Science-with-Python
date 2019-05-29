#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

df = pd.read_excel('Pay_classification.xlsx',header = 0)


# In[2]:


print("The number of rows and columns:",(df.shape))


# In[3]:


df.columns


# In[4]:


#drop null values 
df = df.dropna()


# In[5]:


y = df['Annual_pay']
df = df.drop(columns = ['Annual_pay'])


# In[6]:


df.head()


# In[7]:


#importing LabelEncoder form Sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['education'] = label_encoder.fit_transform(df['education'])


# In[8]:


df['education'].head()


# In[9]:


#splitting Categorical and numerical variables into seperate dataframe
data_column_category = df.select_dtypes(exclude=[np.number]).columns
data_column_numerical = df.select_dtypes(include=[np.number]).columns


# In[12]:


#performing label encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder = LabelEncoder()
for i in data_column_category:
    df[i] = label_encoder.fit_transform(df[i])
    
#Performing Onehot Encoding
onehot_encoder = OneHotEncoder(sparse=False)
onehot_encoded = onehot_encoder.fit_transform(df[data_column_category])

#Creating a dataframe with encoded data with new column name
onehot_encoded_frame = pd.DataFrame(onehot_encoded, columns = onehot_encoder.get_feature_names(data_column_category))
onehot_encoded_frame     


# In[13]:


data_numeric = df.loc[:,data_column_numerical]
data_numeric.head()


# In[14]:


data_numeric.shape


# In[15]:


X = pd.concat([onehot_encoded_frame,data_numeric],axis = 1)


# In[16]:


#Performing Scaling
from sklearn import preprocessing

std_scale = preprocessing.StandardScaler().fit(X)
X_std = std_scale.transform(X)
print(X_std)


# In[17]:


#test train split

from sklearn. model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2, random_state=0)


# In[18]:


print("FULL Dateset X Shape: ", X_std.shape )
print("Train Dateset X Shape: ", X_train.shape )
print("Test Dateset X Shape: ", X_test.shape )


# In[ ]:





# In[ ]:




