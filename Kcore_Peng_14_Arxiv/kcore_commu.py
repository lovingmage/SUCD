'''
   This code is designed and written by Chenghong Wang.
   Do not copy, disclose, or distribute without explicit written permission. 

   Author: 			Chenghong Wang <cwang132@syr.edu>
   
   Instruction:			This program is a python package which is designed to compute the community
				partition by using kcore method. The kore method is to firstly reduce the
				original graph by using kcore method; Then perform community detection method
				on the searched kcore subgraph, then recover the subgraph and the community
				structure.
					
	Usage:			This is a package of kcore community detection, to use all function here, by
				using :

					import kcore_comun
		
				in your python source code
					
'''

import community
import networkx as nx


def kcore_partition(k, FILE_PATH):
#Read Network files as gml file type, create a networkx graph and use the eisted graph file
#Random graph may have poor performance, erdos renyi graph doesn't have true community structure
	G = nx.read_gml(FILE_PATH)
	H = nx.k_core (G, k)
	partition = community.best_partition(H)
	communities = list(set(partition.values()))
	new_partition = {}
	for community_part in communities:
        	new_partition[community_part] = []
	#print new_partition
	for nodes in partition.keys():
        	new_partition[partition[nodes]].append(nodes)
	#print new_partition
	return new_partition
	
if __name__ == '__main__':
	partition = kcore_partition(3,'dolphins.gml')
	print partition

'''
for nodes in G.nodes():
	if nodes not in H.nodes():
		best_mod = 0
		for coms in communities:
			partition[nodes] = coms
			if community.modularity(partition, H) < best_mod:
				del partition[nodes]

print partition
				

def best_partition(G):
	partition = community.best_partition(G)
	communities = list(set(partition.values()))
'''
		
