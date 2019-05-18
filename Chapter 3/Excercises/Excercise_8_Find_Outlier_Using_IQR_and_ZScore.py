import seaborn as sbn
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("german_credit_data.csv")

sbn.boxplot(df['Age'])
plt.show()
from scipy import stats
import numpy as np
threshold = 3
z = np.abs(stats.zscore(df['Age']))

print(np.where(z > 3))

print(z[163])

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1
print(IQR)

df.drop(columns="Unnamed: 0", inplace=True)

df = df.select_dtypes(include=np.number)

Lower_Fence = Q1 - (1.5 * IQR)

Upper_Fence = Q3 + (1.5 * IQR)

print(df[~((df["Age"] < Lower_Fence) |(df["Age"] > Upper_Fence))])

print(df[~(z < 3)])

