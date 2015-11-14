# -*- coding: utf-8 -*-
import numpy as np
import sys
from math import*
import argparse


def jaccard_similarity_coefficient(c_true, c_pred):
    
    """example
    x = {'0':[1,2],'2':[3,4]}
    y = {'0':[1,2],'1':[3,4]}

    print jaccard_similarity_coefficient(x, y)
    
    Jaccard similarity coefficient
    ----------
    The Jaccard similarity coefficient, defined as the size of the intersection 
    divided by the size of the union of two sets, is used to compare the 
    predicted set in c_pred to the corresponding set in c_true.
    This function can be used to calculate the similarity between,for example, the community 
    detection results using k-core/k-truss to the original communitiy detection results.
    The algorithm contains two sets of nested loops. 

    This function, first, iterate over every community Ci in the first dictionary c_true.  
    For each Ci, find the Dj in the second dictionary c_pred that is closest 
    (i.e., has the greatest Jaccard similarity with Ci). 
    
    To do this, iterate over every Dj and calculate the Jaccard similarity with Ci.  
    Let Jacc_i be the Jaccard similarity of Ci and Dj.  In other words, for every 
    community Ci, we're going to find the most similar community from the D communities.  
    If for some Ci, we can find an identical Dj, then Jacc_i = 1.  Then define P 
    to be the average of all these Jacc_i values.  If every community Ci has an 
    identical Dj, then P = 1.

    Next, do the same thing, but reverse the positions of C and D (in other words, 
    iterate over every Dj, and find the closest Ci).  Let R be the average of all 
    the maximum Jaccard scores found in this set of nested loops.  
    If every community Dj has an identical Ci, then R = 1.

    Then define F = 2*(P * R)/(P + R).  This is the harmonic mean of P and R. 
    
    Parameters
    ----------
    c_true : a dictionary with list as the values, e.g. {'0:[1,2],'1':[3,4,5]'}, 
             this can be the original communitiy detection results
    c_pred : a dictionary with list as the values, e.g. {'0:[1,2],'1':[3,4,5]'}, 
             this can be the community detection results using k-core/k-truss, etc.
 
    
    Returns
    -------
    F : float
        The harmonic mean of P and R.   
        
        The best performance is 1 """

    # initlize two array to hold the highest Jaccard similarity coefficient get from  
    # the most similar community from c_pred to c_true and from c_true to c_pred respectively.
    Jxy = [0] * len(c_true)
    Jyx = [0] * len(c_pred)
    i = 0
    j = 0


    #iterate over every community Ci in the first dictionary c_true.  
    #For each Ci, find the Dj in the second dictionary c_pred that is closest
    for keyx in c_true:
        for keyy in c_pred:
            intersection = len(set.intersection(*[set(c_true.get(keyx)), set(c_pred.get(keyy))]))
            union = len(set.union(*[set(c_true.get(keyx)), set(c_pred.get(keyy))]))
            coefficient = intersection/float(union)
            if (coefficient >Jxy[i]):
                Jxy[i] = coefficient
        i = i+1
    
    #iterate over every community Di in the second dictionary c_true.  
    #For each Di, find the Cj in the first dictionary c_true that is closest
    for keyy in c_pred:
        for keyx in c_true:
            intersection = len(set.intersection(*[set(c_true.get(keyx)), set(c_pred.get(keyy))]))
            union = len(set.union(*[set(c_true.get(keyx)), set(c_pred.get(keyy))]))
            coefficient = intersection/float(union)
            if (coefficient >Jyx[j]):
                Jyx[j] = coefficient
        j = j+1
    
    
    P = np.average(Jxy)
    R = np.average(Jyx)
    F = 2*(P*R)/(P+R)
    
    return F
    
if len(sys.argv) < 3:
	print "Please give 2 file names as the arguments"   
file1, file2 = sys.argv[1],sys.argv[2]
c_true = {}
c_pred = {}
with open(file1) as fd1, open(file2) as fd2:
    c_true = eval(fd1.readline())
    c_pred = eval(fd2.readline())


print jaccard_similarity_coefficient(c_true, c_pred)


