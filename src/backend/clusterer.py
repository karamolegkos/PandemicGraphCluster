from sklearn.cluster import KMeans
import numpy as np
from numpy import dot
from numpy.linalg import norm

codes = ['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'NA', 'FI', 'FR', 'DE', 'GR', 'HU', 'IS', 'IE', 'IT', 'LV', 'LI', 'LT', 'LU', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE']

# Function to get the distance between two countries (Not Used)
def cosine_similarity(list_1, list_2):
  cos_sim = dot(list_1, list_2) / (norm(list_1) * norm(list_2))
  return cos_sim

# Function to calculate the euclidean distance between two points
def euclidean_distance(point1, point2):
    squared_diff = [(point2[i] - point1[i]) ** 2 for i in range(len(point1))]
    sum_squared_diff = sum(squared_diff)
    distance = sum_squared_diff ** 0.5

    return distance

def cluster_data(dataset_dict, year, week, num_clusters):
    # Gather all the dicts for the given year and week
    nodes = []
    for code in codes:
        key = (('year', str(year)), ('week', str(week)), ('country_code', code))
        
        if key in dataset_dict:
            values = []
            for inner_key in dataset_dict[key]:
                if inner_key != 'country':
                    values.append(dataset_dict[key][inner_key])

            nodes.append([code, values])
    
    # Create the adjacency matrix
    adjacency_matrix = []
    for node_1 in nodes:
        row = []
        for node_2 in nodes:
            row.append(euclidean_distance(node_1[1], node_2[1]))
        adjacency_matrix.append(row)

    # our adjacency matrix
    """A = np.array([
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]])"""
    # print("Adjacency Matrix:")
    # print(A)
    A = np.array(adjacency_matrix)

    # diagonal matrix
    D = np.diag(A.sum(axis=1))

    # graph laplacian
    L = D-A

    # eigenvalues and eigenvectors
    vals, vecs = np.linalg.eig(L)

    # sort these based on the eigenvalues
    vecs = vecs[:,np.argsort(vals)]
    vals = vals[np.argsort(vals)]

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=num_clusters, n_init='auto')
    kmeans.fit(vecs[:,1:num_clusters])
    colors = kmeans.labels_

    node_codes = []
    for node in nodes:
        node_codes.append(node[0])
    return node_codes, colors