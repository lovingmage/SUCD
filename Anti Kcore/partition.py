# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:20:10 2016

@author: skiph
"""

import community
import networkx as nx
from collections import defaultdict
import sys
#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure

def reverseDict(originalDict):
	newDict = defaultdict(list)
	
	for k, v in originalDict.items():
		newDict[v].append(k)

	return newDict
	
if __name__ == '__main__':


	FILE_PATH = sys.argv[1]
	G = nx.read_edgelist(FILE_PATH)

	partition = community.best_partition(G)
	rpartition = reverseDict(partition)
	list = {}
	for iter in rpartition:
		list[iter] = len(rpartition[iter])
	print list 

