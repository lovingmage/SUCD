import networkx as nx

def anti_kcore(G, k = None, core_number = None):
    if core_number is None:
        core_number = nx.core_number(G)
    if k is None:
        k = max(core_number.values())
    nodes = (n for n in core_number if core_number[n] >= k)
    anti_nodes = (n for n in core_number if core_number[n] < k)
    return (G.subgraph(anti_nodes).copy(), list(nodes))
	
	
    
if __name__ == "__main__":
    FILE_PATH = "./dolphin.txt"
    G = nx.read_edgelist(FILE_PATH)
    
    '''Set Upper Bound Graph Scale'''
    node_size ={0.1, 0.2, 0.3, 0.4, 0.5, 0.6}
    upper_bound = int(0.2 * len(G.nodes()))
    #print upper_bound
    
    resi_node = []
    G1 = G
    
    while len(resi_node) < upper_bound :
        (H, temp) = anti_kcore(G1)
        G1 = H
        resi_node = resi_node + temp
        
    print resi_node
        
    
    

    
    
      