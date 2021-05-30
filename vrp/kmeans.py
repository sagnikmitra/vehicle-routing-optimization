# from sklearn.cluster import KMeans
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# df = pd.DataFrame({
#     'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
#     'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
# })
# kmeans = KMeans(n_clusters=3)
# kmeans.fit(df)

# labels = kmeans.predict(df)
# centroids = kmeans.cluster_centers_
# colmap = {'1': 'r', '2': 'g', '3': 'b'}
# fig = plt.figure(figsize=(5, 5))
# plt.scatter(df['x'], df['y'], cmap='viridis', alpha=0.5, edgecolor='k')
# for centroid in centroids:
#     plt.scatter(*centroid, cmap='viridis')
# plt.xlim(0, 80)
# plt.ylim(0, 80)
# plt.show()

dict = {}
arr = ['s', 't']
for i in range(0, int(len(arr))):
    dict[arr[i]] = arr[i]
print(dict)
