'''
	Script designed and written by Chenghong Wang.
	Do not copy, disclose, or distribute without explicit written permission.

	Author:                      Chenghong Wang <cwang132@syr.edu>

	Instruction:
				This program is a python package which is designed to calculate the eigenvalues
				when perform community detection. It also support Laplacian Matrix generation and
				Normalized Laplacian Matrix generation. The method used for computing the eigenvalues
				contain two method, one is offered by NumPy and another is PowerIteration. The NumPy 
				offered method can compute all eigenvalues of given matrix and all corresponding eigen-
				vectors. The power iteration method only return the dominant eigenvalus.

	Usage:                  This is a package of kcore community detection, to use all function here, by
							using :

'''
import numpy
import random
import scipy.sparse.linalg
from encore.storage.tests.static_url_store_test import count
import scipy
import networkx as nx
import time
import sys


def mult(edge_lists, v):
    x = numpy.zeros((len(edge_lists), 1))
    for row_idx in range(len(v)):
        tot = 0
        for i in edge_lists[row_idx]:
            tot += v[i][0]
        x[row_idx][0] = tot
    return x


def get_egv_powerit(FILE_PATH):
	IN = open(FILE_PATH, 'r')
	read_line = IN.readline()
	index = {}
	count = 0
	edges = {}
	while(read_line):
    		t = read_line.rstrip().split()
    		if len(t) > 0 and t[0] != t[1]:
        		if t[0] not in index:
            			index[t[0]] = count
            			count += 1
            			edges[index[t[0]]] = set([])
        		if t[1] not in index:
            			index[t[1]] = count
            			count += 1
            			edges[index[t[1]]] = set([])
        		edges[index[t[0]]].add(index[t[1]])
        		edges[index[t[1]]].add(index[t[0]])
    		read_line = IN.readline()
	IN.close()

#v is a normalized random vector
	s = len(edges)
	v = numpy.zeros((s, 1))
	for i in range(s):
    		v[i,0] = random.random()

	tot = numpy.linalg.norm(v)    
	for i in range(s):
    		v[i,0] /= tot

	v = numpy.matrix(v)

	start = time.clock()
	for iter_num in range(num_iter): 
    #update the vector and normalize
    		v2 = mult(edges, v)
    		v = v2
    		tot = numpy.linalg.norm(v)    
    		for i in range(s):
        		v[i,0] /= tot
    		print iter_num
	end = time.clock()
	print end - start
	return v

def gen_laplacian(G):
	lap_matrix = nx.laplacian_matrix(G)
	return lap_matrix

def gen_nor_laplacian(G):
	lap_nor_matrix = nx.normalized_laplacian_matrix(G)
	return lap_nor_matrix	




if __name__ == '__main__':
	
	FILE_PATH = sys.argv[1]
	MODE = sys.argv[2]
	
	G = nx.read_edgelist(FILE_PATH)
	M1 = gen_laplacian(G)
	M2placian(G):
        lap_matrix = nx.laplacian_matrix(G)
        return lap_matrix

def gen_nor_laplacian(G):
        lap_nor_matrix = nx.normalized_laplacian_matrix(G)
        return lap_nor_matrix = gen_nor_laplacian(G)
 M1
