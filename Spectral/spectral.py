import sys
import numpy as np
import networkx as nx
from time import clock
from scipy.linalg import eigh as largest_eigh
from scipy.sparse.linalg.eigen.arpack import eigsh as largest_eigsh
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from numpy import linalg as LA


def gen_laplacian(G, _MODE_):
	if _MODE_ == 1:
		return nx.laplacian_matrix(G)
	else:
		return nx.normalized_laplacian_matrix(G)
		
def save_eigen(w, v):
    np.savetxt('eigen_values.csv', w, delimiter=',')
    np.savetxt('eigen_vectors.csv', v, delimiter=',')

if __name__ == "__main__":
    #Read Network files as gml file type, create a networkx graph and use the eisted graph file
	#Random graph may have poor performance, erdos renyi graph doesn't have true community structure
    
	#Start log file, create log file and start.
	FILE_PATH = sys.argv[1]
	#_MODE_ = sys.argv[2]
	G = nx.read_edgelist(FILE_PATH)
	
	Lap = gen_laplacian(G, 2)
	w, v = LA.eig(Lap.todense())
	
	#m, n = Lap.shape
	#print Lap.todense()
	#evals_large, evecs_large = largest_eigh(Lap, eigvals=(Lap.size-k,Lap.size-1))
	save_eigen(w, v)
