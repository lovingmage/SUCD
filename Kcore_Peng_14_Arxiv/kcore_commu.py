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

					In Linux Command Line using the following command
					
					$python kcore_comm.py [INPUT_FILE_TYPE] [Kcore Number]
					
'''

import community
import networkx as nx
from collections import Counter

import sys

	
	
def convert_partition_format(original_partition):
#Read Network files as gml file type, create a networkx graph and use the eisted graph file
#Random graph may have poor performance, erdos renyi graph doesn't have true community structure
	#partition = community.best_partition(H)
	communities = list(set(partition.values()))
	new_partition = {}
	for community_part in communities:
        	new_partition[community_part] = []
	#print new_partition
	for nodes in partition.keys():
        	new_partition[partition[nodes]].append(nodes)
	#print new_partition
	return new_partition
	

def sort_by_neighbor(H, G):
	neighbor_dict = {}
	sorted_neighbor = []
	for node in G.nodes():
		if node not in H.nodes():
			count = 0
			for neighbors in G.neighbors(node):
				if neighbors in H:
					count = count + 1
			neighbor_dict[node] = count
		else: 
			continue
	#print neighbor_dict 
	sorted_neighbor_pair = sorted(neighbor_dict.iteritems(), key=lambda d:d[1], reverse = True )  
	#print sorted_neighbor_pair
	for node_pair_index in range (0, len(sorted_neighbor_pair), 1):
		sorted_neighbor.append(sorted_neighbor_pair[node_pair_index][0])
	#print sorted_neighbor
	return sorted_neighbor
		

def vote_for_node(kcore_partition, sorted_recover_nodes, G):
	rec_partition = kcore_partition
	for node in sorted_recover_nodes:
		vote_list = []
		for neighbor in G.neighbors(node):
			if neighbor not in rec_partition.keys():
				continue
			else:
				vote_list.append(kcore_partition[neighbor])
		#print vote_list
		vote_dic = Counter(vote_list)
		#print vote_dic
		vote_dic_sorted = sorted(vote_dic.iteritems(), key=lambda d:d[1], reverse = False )
		#print vote_dic_sorted
		if not vote_dic_sorted:
			rec_partition = -1
		else:
			rec_partition[node] = vote_dic_sorted[0][0]
	return rec_partition	



if __name__ == '__main__':

	command2 = sys.argv[1]
	command3 = sys.argv[2]
	G = nx.read_gml(command2)
	H = nx.k_core (G, int(command3))
	#kcore_partition = kcore_partition(H)
	partition = community.best_partition(H)
	sorted_recover_nodes = sort_by_neighbor(H, G)
	#print sorted_recover_nodes
	vote_for_node(partition, sorted_recover_nodes, G)
	new_partition = vote_for_node(partition, sorted_recover_nodes, G)

	print new_partition
		
