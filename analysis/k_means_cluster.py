import numpy as np
from sklearn.cluster import KMeans
import plotly.express as px
from collection import data

filtered_data = data[data['year'] >= 2019].copy()

# KMeans clustering on L* only
X = filtered_data[['L']].values
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
filtered_data['cluster'] = kmeans.fit_predict(X)

# Sort clusters by luminance centroid (so 0 = darkest, 2 = lightest)
centroids = kmeans.cluster_centers_.flatten()
sorted_indices = np.argsort(centroids)
cluster_mapping = {old: new for new, old in enumerate(sorted_indices)}
filtered_data['cluster'] = filtered_data['cluster'].map(cluster_mapping)

cluster_labels = {
    0: 'Darker',
    1: 'Medium',
    2: 'Lighter'
}
filtered_data['cluster_label'] = filtered_data['cluster'].map(cluster_labels)

fig = px.scatter(
    filtered_data,
    x='year',
    y='L',
    color='cluster_label',
    symbol='role',
    hover_data=['role', 'year', 'L'],
    title='K-Means Clustering of Luminance (2019–2024)',
    labels={'L': 'Luminance (L*)', 'year': 'Year', 'cluster_label': 'Skin Tone Cluster'}
)

fig.update_traces(marker=dict(size=10))
fig.update_layout(
    height=600,
    legend_title="Cluster (Skin Tone)"
)

fig.show()