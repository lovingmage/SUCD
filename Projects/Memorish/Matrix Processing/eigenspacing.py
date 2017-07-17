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

def statistic_random_matrix(mat_size, REPS, sample_percent):
    matrix_size = mat_size
    record_dict = {}

    for j in range(1, REPS, 1):
        random_matrix = np.random.randint(2, size = (matrix_size, matrix_size))
        w, v = LA.eig(random_matrix)

        for i in range(1, int(sample_percent * matrix_size), 1):
            if w[i] > 0:
                eigen_spacing = np.absolute(w[i] - w[i+1])
                record_dict[w[i]] = eigen_spacing
        
#sorted_data = sorted(record_dict.items(), key=lambda items: items[1])

    plt.plot(record_dict.keys(), record_dict.values(), 'rx', markersize = 3.3)
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
    

def statistic_matrix(mat):
    w, v = LA.eig(mat)
    record_dict = {}
    
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
    file_list=[
            "facebook_combined.txt", 
            "com-amazon.all.dedup.cmty.txt", 
            "email-Enron.txt", 
            "com-amazon.ungraph.txt", 
            "com-dblp.ungraph.txt",
            "ca-AstroPh.txt",
            "ca-CondMat.txt",
            "ca-GrQc.txt",
            "ca-HepPh.txt",
            "ca-HepTh.txt",
            "email-Enron.txt"]
    
    file_name = "/Users/lovingmage/Downloads/data/" + file_list[9]
    G=nx.read_edgelist(file_name)
    npmat = nx.to_numpy_matrix(G, G.nodes())
    
    eigen_spacing_plots(npmat, file_list[9])
    
    '''
    eigspacs = eigen_spacing_distribution(npmat)


    '''
    
    
