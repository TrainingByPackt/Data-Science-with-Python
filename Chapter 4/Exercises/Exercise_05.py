# Exercise 5: Assigning Predicted Clusters to Observations

# get predicted labels
labels = model.labels_

# see how many of each label we have
import pandas as pd
pd.value_counts(labels)

# add label to df_shuffled
df_shuffled['Predicted_Cluster'] = labels
print(df_shuffled.head(5))

