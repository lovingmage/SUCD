#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:52:44 2017

@author: lovingmage
"""
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import networkx as nx
import scipy.sparse as sparse
from scipy.optimize import curve_fit


def statistic_random_matrix(mat_size, REPS):
    matrix_size = mat_size
    record_dict = {}

    for j in range(1, REPS, 1):
        #random_matrix = np.random.randint(2, size = (matrix_size, matrix_size))
        random_matrix = np.random.rand(matrix_size, matrix_size)
        w, v = LA.eig(random_matrix)
        w = np.sort(w)
        w = w[::-1]

        for i in range(1, matrix_size - 1, 1):
            if w[i] > 0:
                eigen_spacing = w[i] - w[i+1]
                record_dict[w[i]] = eigen_spacing
        
#sorted_data = sorted(record_dict.items(), key=lambda items: items[1])
    params = curve_fit(fitfunc, record_dict.keys(), record_dict.values())
    print params[0]

    plt.plot(record_dict.keys(), record_dict.values(), 'rx', markersize = 3.3)
    plt.ylabel("associated eigenspacing")
    plt.xlabel("eigenvalue")
    tittle = "eigenvalue v.s. associated eigenspacing " + "matrix size " + str(mat_size)
    plt.title(tittle)
    plt.show()
    
    
def rd_eigen_spacing_distribution(mat_size, REPS):
    matrix_size = mat_size
    eigenspacings = []

    for j in range(1, REPS, 1):
        random_matrix = np.random.randint(2, size = (matrix_size, matrix_size))
        w, v = LA.eig(random_matrix)
        
        for i in range(1, matrix_size - 1, 1):
            if w[i] > 0:
                eigen_spacing = np.absolute(w[i] - w[i+1])
                eigenspacings.append(eigen_spacing)
                
    return sorted(eigenspacings)
        
    
    
    
    '''
    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10,8,6,4,2,1]
 
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')
    '''
 
def eigen_spacing_distribution(mat):
    eigenspacings = []
    w, v = LA.eig(mat)
    
    eigen_size = w.size
        
    for i in range(1, eigen_size - 1, 1):
        if w[i] > 0:
            eigen_spacing = np.absolute(w[i] - w[i+1])
            eigenspacings.append(eigen_spacing)
            
    plt.hist(eigenspacings, bins = 100)
    plt.ylabel("eigenspacing counts")
    plt.xlabel("eigenspacing")
    tittle = "Eigenspacing Distribution" 
    plt.title(tittle)
    plt.show()
    
def fitfunc(x, a, b, c):
    return a * np.exp(np.multiply(b, x)) + c

def statistic_matrix(mat, fname, mode):
    w, v = sparse.linalg.eigsh(mat, k=100)
    w = np.sort(w)
    w = w[::-1]
    
    record_dict = {}

    eigen_size = w.size
    for i in range(mode, eigen_size - 1, 1):
        if w[i] > 0:
            eigen_spacing = w[i] - w[i+1]
            record_dict[w[i]] = eigen_spacing
        
    #print record_dict
    del record_dict[min(record_dict.keys())]    
    params = curve_fit(fitfunc, record_dict.keys(), record_dict.values())
    plt.plot(record_dict.keys(), record_dict.values(), 'rx', markersize = 3.3)
    #plt.plot(record_dict.keys(), fitfunc(record_dict.keys(), 0.00899265, 0.64684346, -0.10575506), 'r-', label='fit')
    #plt.yscale('log')
    #plt.xscale('log')
    print params[0]
    
    plt.ylabel("associated eigen_spacing")
    plt.xlabel("eigv")
    tittle = "eigv v.s. eigs " + fname
    plt.title(tittle)
    str_out = "/Users/lovingmage/Downloads/data/plots/top_100_gen/" + fname + ".png"
    plt.savefig(str_out)

    
    
def eigen_spacing_plots(mat, file_name):
    eigenspacings = []
    record_dict = {}
    w, v = LA.eig(mat)
    eigen_size = w.size
        
    for i in range(1, eigen_size - 1, 1):
        if w[i] > 0:
            eigen_spacing = np.absolute(w[i] - w[i+1])
            eigenspacings.append(eigen_spacing)
            
    plt.hist(eigenspacings, bins = 100)
    plt.ylabel("eigenspacing counts")
    plt.xlabel("eigenspacing")
    tittle = "Eigenspacing_Distribution_of_" + file_name
    plt.title(tittle)
    plt.show()

    
    plt.hist(eigenspacings, bins=100, normed=True, cumulative=True)
    plt.ylabel("eigenspacing counts")
    plt.xlabel("eigenspacing")
    tittle = "Cumulative Distribution of " + file_name
    plt.title(tittle)
    plt.show()
    
    eigen_size = w.size
    for i in range(0, eigen_size - 1, 1):
        if w[i] > 0:
            eigen_spacing = np.absolute(w[i] - w[i+1])
            record_dict[w[i]] = eigen_spacing
        

    plt.plot(record_dict.keys(), record_dict.values(), 'rx', markersize = 3.3)
    plt.ylabel("associated eigen_spacing")
    plt.xlabel("eigv")
    tittle = "eigv v.s. associated eigen_spacing"
    plt.title(tittle)
    plt.show()
    
    
if __name__ == "__main__":
    
    
    '''
    node_num = 3000
    mode = 0
    m = 15
    pr = 0.3
    G = nx.barabasi_albert_graph(3000, m)
    npmat = nx.to_numpy_matrix(G, G.nodes())
    str_tittle = "ba_300_3000_r:" + str(pr) + "_m:"+ str(m)+ "_mode:" + str(mode)
    statistic_matrix(npmat, str_tittle, 1)
    '''
    
    file_list=[
            "com-amazon.ungraph.txt", 
            "com-dblp.ungraph.txt",
            "ca-AstroPh.txt",
            "ca-CondMat.txt",
            "ca-HepPh.txt",
            "ca-GrQc.txt",
            "ca-HepTh.txt",
            "email-Enron.txt",
            "facebook_combined.txt",
            "adjnoun.txt",
            "dolphins.txt",
            "netscience.txt",
            "power.txt"]
    '''
    file_name = "/Users/lovingmage/Downloads/data/" + file_list[-1]
    G=nx.read_edgelist(file_name)
    npmat = nx.to_numpy_matrix(G, G.nodes())
    statistic_matrix(npmat, file_list[-2], 0)
    '''
    
    statistic_random_matrix(1000,2)
    
   
