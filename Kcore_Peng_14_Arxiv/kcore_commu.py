'''
   This code is designed and written by Chenghong Wang.
   Do not copy, disclose, or distribute without explicit written permission. 

   Author: 			Chenghong Wang <cwang132@syr.edu>
   
   Instruction:		This program is a multiprocessor programming code to multiply 
					two matrixes, in this code we use POSIX pthread api to perform 
					parallel programming.
					
	Usage:			Compile the matrix.c under Linux system use the following command:
					$ gcc -pthread -o matrix.out matrix.c
					After compile, you can run it with:
					$ ./matrix.out
					
	Comment:		If you want to modify the scale of current matrix you should change 
					the matrix define part in this code followed the instruction in that 
					section.
'''

import community
import networkx as nx
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt


#Read Network files as gml file type, create a networkx graph and use the eisted graph file
#Random graph may have poor performance, erdos renyi graph doesn't have true community structure
G = nx.read_gml('dolphins.gml')
H = nx.k_core (G,3)
#Compute the best partition by using louvain method
print G.nodes()
print H.nodes()
partition = community.best_partition(H)

#print partition.values()
#print partition[34]
#Plot the result
#values = [partition.get(node) for node in H.nodes()]
#print H.number_of_nodes()

#nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
#plt.savefig('dolphinKcore3')

#print partition.values()
communities = list(set(partition.values()))
print communities

for nodes in G.nodes():
	if nodes not in H.nodes():
		best_mod = 0
		for coms in communities:
			partition[nodes] = coms
			if community.modularity(partition, H) < best_mod:
				del partition[nodes]

print partition
				


