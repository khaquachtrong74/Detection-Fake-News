from sklearn.cluster import KMeans
import numpy as np

# Giả sử bạn có một mảng dữ liệu X
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0],
              [10, 10], [10, 12], [10, 8],
              [13, 10], [13, 12], [13, 8]])

# Tạo và huấn luyện mô hình KMeans với 3 cụm
num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)
import matplotlib.pyplot as plt


