import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Sample vendor names (you can replace this list with your data)
vendor_names = [
    "Apple Inc.",
    "Apple",
    "Apple Co.",
    "Microsoft Corp.",
    "Microsoft Inc.",
    "Microsoft",
    "Samsung Electronics",
    "Samsung",
    "Samsung Corp.",
    "Sony Corporation",
    "Sony"
]

# 1. Preprocess vendor names: Convert to lowercase and strip whitespaces
preprocessed_names = [name.lower().strip() for name in vendor_names]

# 2. Convert vendor names into a matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_names)

# 3. Cluster the vendor names
# For this example, let's assume we want 4 clusters (you can change this number)
n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(X)

# Print the clusters
for i in range(n_clusters):
    print(f"Cluster {i + 1}:")
    for idx, label in enumerate(clusters):
        if label == i:
            print(f"  {vendor_names[idx]}")
    print("")

# Optionally, if you'd like to evaluate the clustering
sil_score = silhouette_score(X, clusters)
print(f"Silhouette Score: {sil_score:.2f}")
