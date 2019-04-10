# Exercise 10: Visual Comparison of Inertia by n_clusters

# Continuing from Activity 3

# plot inertia by n_clusters with both lines
import matplotlib.pyplot as plt
x = list(range(1,len(mean_inertia_list_PCA)+1))
y = mean_inertia_list_PCA
y2 = mean_inertia_list 
plt.plot(x, y, label='PCA')
plt.plot(x, y2, label='No PCA')
plt.title('Mean Inertia by n_clusters for Original Features and PCA Transformed Features')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Inertia')
plt.legend()
plt.show()