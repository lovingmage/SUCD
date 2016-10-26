# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 17:48:57 2016

@author: skiph
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy

G = nx.read_gml('dolphins.gml')
H = nx.k_core(G, 2)
out = nx.to_numpy_matrix(H)

dic = {}
for i in range(0, len(out), 1):
    count = 0    
    for j in range(0, len(out), 1):
        if out[i,j] == 0.0:
            count = count + 1
            continue
        if out[i, j] == 1.0:
            break
    dic[i] = count
    
sortlist = sorted(dic.iteritems(), key=lambda d:d[1], reverse = False )

storetmp = []
for ite in range(0, len(sortlist), 1):
    storetmp.append(sortlist[ite][0])
    
#print len(storetmp)
    

nx = numpy.matrix(out[storetmp[0]])
for i in range(1, len(out), 1):
    nx = numpy.row_stack((nx, out[storetmp[i]]))
        
    
plt.imshow(nx, cmap='hot', interpolation='nearest')
plt.show()
