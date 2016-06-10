# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:20:10 2016

@author: skiph
"""

import community
import networkx as nx
<<<<<<< HEAD
import matplotlib.pyplot as plt
import json
=======
from collections import defaultdict
>>>>>>> master
import sys
#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure

<<<<<<< HEAD
FILE_PATH = sys.argv[1]
G = nx.read_edgelist(FILE_PATH)

#first compute the best partition
partition = community.best_partition(G)
outPartition = json.dumps(partition)  
print outPartition
json.dump(outPartition, open('original_partition.dat', 'w'))
#drawing
#values = [partition.get(node) for node in G.nodes()]

#nx.draw_spring(G, scale = 0.5, cmap = plt.get_cmap('jet'), node_color = values, node_size=60, with_labels=False)
#plt.savefig('original.png')
=======
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

>>>>>>> master
