# Exercise 5: Plotting Mean Inertia by n_clusters

# plot inertia by n_clusters
import matplotlib.pyplot as plt
x = list(range(1, len(mean_inertia_list)+1))
y = mean_inertia_list
plt.plot(x, y)
plt.title('Mean Inertia by n_clusters')
plt.xlabel('n_clusters')
plt.xticks(x)
plt.ylabel('Mean Inertia')
plt.show()

