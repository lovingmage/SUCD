import sys
import numpy as np
import networkx as nx
from time import clock
from scipy.linalg import eigh as largest_eigh
from scipy.sparse.linalg.eigen.arpack import eigsh as largest_eigsh
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from numpy import linalg as LA
from sklearn.metrics import jaccard_similarity_score
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.cluster import SpectralClustering


def gen_laplacian(G, _MODE_):
    if _MODE_ == 1:
        return nx.laplacian_matrix(G)
        else:
            return nx.normalized_laplacian_matrix(G)

def save_eigen(w, v, FILE_PATH):
    str_log = FILE_PATH.split('/')[-1]
    
    np.savetxt("eigenvalues.csv", w, delimiter=',')
    np.savetxt("eigenvectors.csv", v, delimiter=',')


if __name__ == "__main__":
    #Read Network files as gml file type, create a networkx graph and use the eisted graph file
    #Random graph may have poor performance, erdos renyi graph doesn't have true community structure
    
    #Start log file, create log file and start.
    FILE_PATH = sys.argv[1]
    pre_clus = sys.argv[2]
    eigv_path = sys.argv[3]
        
    G = nx.read_edgelist(FILE_PATH)
        
    Lap = gen_laplacian(G, 2)
    w, v = LA.eig(Lap.todense())
    save_eigen(w, v, FILE_PATH)
        
    feature_matrix = np.transpose(v)
    partition_orig = KMeans(n_clusters=int(pre_clus)).fit(feature_matrix)
        
    ext_matrix = np.genfromtxt (eigv_path, delimiter=",")
    feature_ext_matrix = np.transpose(ext_matrix)
    partition_fast = KMeans(n_clusters = int(pre_clus)).fit(feature_ext_matrix)
    print partition_orig.inertia_
    print jaccard_similarity_score(partition_orig.labels_, partition_fast.labels_)
    print normalized_mutual_info_score(partition_orig.labels_, partition_fast.labels_)

  '''
    #spec_matrix1 = SpectralClustering(n_clusters=int(pre_clus)).fit(nx.to_numpy_matrix(G))
    spec_matrix = SpectralClustering(n_clusters = int(pre_clus)).fit(nx.to_numpy_matrix(G))
    kmeans_matrix = KMeans(n_clusters = int (pre_clus)).fit(nx.to_numpy_matrix(G))
    print kmeans_matrix.inertia_
    print normalized_mutual_info_score(spec_matrix1.labels_, kmeans_matrix.labels_)
    '''

