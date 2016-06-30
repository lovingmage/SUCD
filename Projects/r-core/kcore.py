import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import community
import json
import sys
import os

if __name__ == "__main__":
    
    FILE_PATH = sys.argv[1]
    node_size = int(sys.argv[2])
    G = nx.read_edgelist(FILE_PATH)


    upper_bound = int(0.1 * node_size * len(G.nodes()))
    #print len(G.nodes())
    core_number = nx.core_number(G)
    #print core_number
    k = max(core_number.values())
    #print k
   
    H = nx.k_core(G,k)
    #print len(H)    
    while(len(H.nodes()) < upper_bound and k > 0) :
	  k = k - 1
	  H = nx.k_core(G,k)
    
 
    partition = community.best_partition(H)
    for key in partition.keys():
        print key    
    '''
    partition = community.best_partition(H)
    outPartition = json.dumps(partition)  
    json.dump(outPartition, open('k11.dat', 'w'))
    

    values = [partition.get(node) for node in H.nodes()]

    nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color = values, node_size=50, with_labels=False)    
    
    #nx.draw_spring(M, node_size=50, with_labels=False)
    plt.savefig('c-kl11')
    '''
