# Unsupervised Learning

# Hierarchical Cluster Analysis (HCA)

# import data
from sklearn import datasets
iris = datasets.load_iris()

# save the data as df
import pandas as pd
df = pd.DataFrame(iris.data)

# explore data dimensions
n_rows = df.shape[0]
n_columns = df.shape[1]
print('There are {} rows and {} columns in the Iris data set'.format(n_rows, n_columns))

# get df info
print(df.info())

# shuffle df
from sklearn.utils import shuffle
df_shuffled = shuffle(df, random_state=42)

# standardize and fit model
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit scaler to the features
scaler.fit(df_shuffled)
# Transform features to scaled version
scaled_features = scaler.transform(df_shuffled)

# create linkage model
from scipy.cluster.hierarchy import linkage 
model = linkage(scaled_features, method='complete') 

# plot dendrogram
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram
plt.figure(figsize=(10,5))
plt.title('Dendrogram')
dendrogram(model,
           leaf_rotation=90,
           leaf_font_size=6)
plt.show()

# get labels
from scipy.cluster.hierarchy import fcluster 
labels = fcluster(model, t=5, criterion='distance') # don't merge clusters further aprt than 5 (see dendrogram)
print(labels)

# assign labels array as a column in df_shuffled
df_shuffled['Predicted_Cluster'] = labels



