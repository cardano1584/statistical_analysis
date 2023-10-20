import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Read vendor names from a CSV file
vendor_names = []
with open('vendor_names.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        vendor_names.append(row['VendorName'])

# 1. Preprocess vendor names: Convert to lowercase and strip whitespaces
preprocessed_names = [name.lower().strip() for name in vendor_names]

# 2. Convert vendor names into a matrix
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_names)

# Find optimal number of clusters using the elbow method
inertias = []
max_clusters = 10  # you can change this if you expect more clusters
for i in range(1, max_clusters+1):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

# Plot the inertia
plt.figure()
plt.plot(range(1, max_clusters+1), inertias, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal Number of Clusters')
plt.show()

# You'll need to visually inspect the plot to determine the elbow.
# Once you've determined the optimal number of clusters, you can run the KMeans clustering with that number:

n_clusters = int(input("Enter the optimal number of clusters (based on the elbow plot): "))
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
clusters = kmeans.fit_predict(X)

# Print the clusters
for i in range(n_clusters):
    print(f"Cluster {i + 1}:")
    for idx, label in enumerate(clusters):
        if label == i:
            print(f"  {vendor_names[idx]}")
    print("")
