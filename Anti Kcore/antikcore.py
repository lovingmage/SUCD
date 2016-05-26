import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def anti_kcore(G, k = None, core_number = None):
    if core_number is None:
        core_number = nx.core_number(G)
    if k is None:
        k = max(core_number.values())
    nodes = (n for n in core_number if core_number[n] >= k)
    anti_nodes = (n for n in core_number if core_number[n] < k)
    return (G.subgraph(anti_nodes).copy(), list(nodes))
	
	
    
if __name__ == "__main__":
    FILE_PATH = "./test.txt"
    G = nx.read_edgelist(FILE_PATH)
    
    '''Set Upper Bound Graph Scale'''
    node_size ={0.1, 0.2, 0.3, 0.4, 0.5, 0.6}
    upper_bound = int(0.2 * len(G.nodes()))
    #print upper_bound
    
    
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
        
    
    print len(G.nodes())
    M = G.subgraph(resi_node).copy()
    
    print len(M.nodes())
    
    nx.draw_spring(M)
    plt.savefig('dl0-2')

    
 