# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:43:14 2017

@author: lovingmage
"""

import numpy as np
import scipy.io
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse


'''
This Function is used to initialize the linear equation,
also set the approximation eigenvalue, and return 
    1.  Matrix A - lambda*I,
    2.  approximation eigenvalue,
    3.  real eigenvector

'''
def initialize_linear_equation(MATRIX_PATH):
    # Read Matrix from Mat files
    x = scipy.io.loadmat(MATRIX_PATH)
    A = x['A']
    MATRIX_SIZE = len(A)
    I = np.identity(MATRIX_SIZE)
    
    # Calculate the eigenvalues and initialize the approximate eigenvalue
    a, b = np.linalg.eig(A)
    eigen = a[0] - 0.05
    # Create Matrxi A - lambda*I
    E = A - eigen*I
    return E, eigen, b[:,0]



'''
This function will repeatly calculating the eigenvector by using 
inverse power method until the result convergent and keep stable.
'''
def inverse_power(E):
    
    MATRIX_SIZE = len(E)
    
    rx = np.random.rand(1, MATRIX_SIZE)
    r0 = rx[0]
    w0 = np.linalg.solve(E, r0)    
    r = w0/max(abs(w0))

    w = np.linalg.solve(E, r)
    
    #Start the inverse_power until convergence
    M =  np.array([w0, w])
    M_sparse = sparse.csr_matrix(M)
    similarities = cosine_similarity(M)
    #print similarities
    
    count = 0
    while (similarities[0][1] < 0.9999999999999999999995):
        w0 = w
        
        w = np.linalg.solve(E, r)
        r = w/max(abs(w))
        M =  np.array([w0, w])
        M_sparse = sparse.csr_matrix(M)
        similarities = cosine_similarity(M_sparse)
        count = count + 1
        
    return w, count
        
        
# Start Function

PATH = 'matlab.mat'
E, eigen_a, eigev = initialize_linear_equation(PATH)
w, c = inverse_power(E)
M =  np.array([w, eigev])
M_sparse = sparse.csr_matrix(M)
similarities = cosine_similarity(M)
print similarities



