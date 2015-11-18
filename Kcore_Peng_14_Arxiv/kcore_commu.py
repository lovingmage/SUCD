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

	
#############################################################################################
#	Function : convert_partition_format( ORIGINAL_PARTITION ):			
#											
#											
#	This function will convert Partition Format from the original format 		
#	to the one which we will used in community similarity comparison process.	
#############################################################################################
	
def convert_partition_format(original_partition):
	communities = list(set(partition.values()))
	new_partition = {}
	for community_part in communities:
        	new_partition[community_part] = []
	#print new_partition
	for nodes in partition.keys():
        	new_partition[partition[nodes]].append(nodes)
	#print new_partition
	return new_partition



##############################################################################################
#       Function : sort_by_neighbor( Kcore Subgraph H, Oroginal Graph G ):		     
#											     
#											
#       This function will sort the recover nodes based on the inside-kcore neighbors,  
#       the function will receive two graph H and G, and then return the asscending     
#	ordered nodes sequence which need to be recovered.			        
##############################################################################################
	
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
		


##############################################################################################
#       Function : vote_for_node( kcore partition kcore_partition, 
#				  sort order recover nodes sorted_recover_nodes,
#				  Original Graph G ):                   
#                                                                                            
#                                                                                       
#       This function is the main function to recover the nodes into current partition,
#	It will retuen a recovered partition dictionary, and if some nodes can not be 
#	recovered, it will divide them into -1 community                              
##############################################################################################


def vote_for_node(kcore_partition, sorted_recover_nodes, G):
	#rec_partition = kcore_partition
	for node in sorted_recover_nodes:
		vote_list = []
		for neighbor in G.neighbors(node):
			if neighbor not in kcore_partition.keys():
				continue
			else:
				vote_list.append(kcore_partition[neighbor])
		#print vote_list
		vote_dic = Counter(vote_list)
		#print vote_dic
		vote_dic_sorted = sorted(vote_dic.iteritems(), key=lambda d:d[1], reverse = False )
		#print vote_dic_sorted
		if not vote_dic_sorted:
			kcore_partition[node] = -1
		else:
			kcore_partition[node] = vote_dic_sorted[0][0]
	return kcore_partition	



if __name__ == '__main__':

	command2 = sys.argv[1]
	command3 = sys.argv[2]
	#Read Network files as gml file type, create a networkx graph and use the eisted graph file
	#Random graph may have poor performance, erdos renyi graph doesn't have true community structure
	G = nx.read_gml(command2)
	H = nx.k_core (G, int(command3))
	print len(H.nodes())
	#kcore_partition = kcore_partition(H)
	partition = community.best_partition(H)
	#print partition 
	sorted_recover_nodes = sort_by_neighbor(H, G)
	#print sorted_recover_nodes
	vote_for_node(partition, sorted_recover_nodes, G)
	new_partition = vote_for_node(partition, sorted_recover_nodes, G)
	print len(new_partition.keys())
	convert = convert_partition_format(new_partition)
	print len(convert[-1])	
