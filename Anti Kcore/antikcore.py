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
    (H, kcore_list) = anti_kcore(G)
    print H.nodes()
    print kcore_list
    
    (M, kcore_list2) = anti_kcore(H)
    print M.nodes()
    print kcore_list2

    
    
      