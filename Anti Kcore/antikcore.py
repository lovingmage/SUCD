import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import community
import json
import sys

def anti_kcore(G, k = None, core_number = None):
    if core_number is None:
        core_number = nx.core_number(G)
    if k is None:
        k = max(core_number.values())
    nodes = (n for n in core_number if core_number[n] >= k)
    anti_nodes = (n for n in core_number if core_number[n] < k)
    return (G.subgraph(anti_nodes).copy(), list(nodes))
	
 
def resi_core(G):
    resi_node = []
    G1 = G
      
    while (len(resi_node) < upper_bound) :
        (H, temp) = anti_kcore(G1)
        G1 = H
        resi_node = resi_node + temp
        
    return G.subgraph(resi_node).copy()
     
	
    
if __name__ == "__main__":
    FILE_PATH = sys.argv[1]
    
    G = nx.read_edgelist(FILE_PATH)
    node_size = int(sys.argv[2])
    '''Set Upper Bound Graph Scale'''
    upper_bound = int(0.1 * node_size * len(G.nodes()))
    
    
    M = resi_core(G)
    #nx.draw_spring(G)
    #plt.savefig('origin')
    
    '''
    (H, temp) = anti_kcore(G)
    M = G.subgraph(temp)
    
    nx.draw_spring(M)
    plt.savefig('dl2')
    '''
    
    
    resi_node = []
    G1 = G
      
    while (len(resi_node) < upper_bound) :
        (H, temp) = anti_kcore(G1)
        G1 = H
        resi_node = resi_node + temp
        

    M = G.subgraph(resi_node).copy()
#    print len(M)

    partition = community.best_partition(M)
    for key in partition.keys():
		print key  
 
    '''outPartition = json.dumps(partition)  
    json.dump(outPartition, open(sys.argv[1]+".dat", 'w'))
    

    values = [partition.get(node) for node in M.nodes()]

    nx.draw_spring(M, cmap = plt.get_cmap('jet'), node_color = values, node_size=50, with_labels=False)    
    
    #nx.draw_spring(M, node_size=50, with_labels=False)
    plt.savefig('c-dl' + sys.argv[1])'''

    
 
