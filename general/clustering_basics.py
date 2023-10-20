import nltk
from nltk.util import ngrams
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

nltk.download('punkt')

def jaccard_distance(str1, str2, n=3):
    """Calculate Jaccard distance between two strings using n-grams."""
    s1 = set(ngrams(str1, n))
    s2 = set(ngrams(str2, n))
    return 1 - float(len(s1 & s2)) / float(len(s1 | s2))

def create_distance_matrix(strings, n=3):
    """Generate a matrix of Jaccard distances between each pair of strings."""
    num_strings = len(strings)
    distance_matrix = np.zeros((num_strings, num_strings))
    
    for i in range(num_strings):
        for j in range(num_strings):
            distance_matrix[i][j] = jaccard_distance(strings[i], strings[j], n)
    
    return distance_matrix

def cluster_strings(strings, t=0.6, n=3):
    """Cluster strings using hierarchical clustering and Jaccard distance."""
    distance_matrix = create_distance_matrix(strings, n)
    
    linkage_matrix = linkage(distance_matrix, method="single")
    
    plt.figure(figsize=(10, 5))
    dendrogram(linkage_matrix, labels=strings)
    plt.title("Hierarchical Clustering of Vendor Names")
    plt.show()
    
    labels = fcluster(linkage_matrix, t, criterion='distance')
    clusters = {}
    for i, label in enumerate(labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(strings[i])
    
    return clusters

# Example vendor names with variations
vendor_names = [
    "Apple Inc.",
    "Apple Incorporated",
    "Apple",
    "Microsoft Corp.",
    "Microsoft Corporation",
    "Google LLC",
    "Goog LLC",
    "Amazon",
    "Amazone"
]

clusters = cluster_strings(vendor_names, t=0.6)
for cluster_id, names in clusters.items():
    print(f"Cluster {cluster_id}: {', '.join(names)}")
