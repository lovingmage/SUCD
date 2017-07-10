#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 21:52:44 2017

@author: lovingmage
"""
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt


matrix_size = 3000
record_dict = {}

for j in range(1, 20, 1):
    random_matrix = np.random.randint(2, size = (matrix_size, matrix_size))
    w, v = LA.eig(random_matrix)

    for i in range(1, matrix_size - 1, 1):
        eigen_spacing = np.absolute(w[i] - w[i+1])
        record_dict[w[i]] = eigen_spacing
        
#sorted_data = sorted(record_dict.iteritems(), key=lambda (k,v): (v,k))

plt.plot(record_dict.keys(), record_dict.values(), 'rx', markersize = 3.3)
plt.show()