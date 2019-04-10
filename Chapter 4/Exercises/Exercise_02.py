# Exercise 2: Plotting HCA Model

# plot dendrogram
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram
plt.figure(figsize=(10,5))
plt.title('Dendrogram for Glass Data')
dendrogram(model,
           leaf_rotation=90,
           leaf_font_size=6)
plt.show()

