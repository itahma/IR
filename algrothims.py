import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.cluster import KMeans
from sklearn.decomposition import LatentDirichletAllocation



#Algorithms

# Clustering
num_clusters = 5  # Set the number of clusters as desired
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(tfidf_matrix)


#Query Suggestion
query_cluster = cluster_labels[most_similar_document_index]
cluster_indices = [i for i, label in enumerate(cluster_labels) if label == query_cluster]
print("The result of Query Suggustion Algorithm search : ",len(cluster_indices))
cluster_similarities = cosine_similarities[0, cluster_indices]
sorted_indices = np.array(cluster_indices)[np.argsort(cluster_similarities)[::-1]]
predicted_documents += [keys[idx] for idx in sorted_indices]



# Topic Detection
num_topics = 3  # Set the number of topics as desired
lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
topic_weights = lda.fit_transform(tfidf_matrix)


