import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import community
import json


if __name__ == "__main__":
    
    FILE_PATH = "./grad_edges"
    G = nx.read_edgelist(FILE_PATH)
    H = nx.k_core(G, 11)
    
    partition = community.best_partition(H)
    outPartition = json.dumps(partition)  
    json.dump(outPartition, open('k11.dat', 'w'))
    

    values = [partition.get(node) for node in H.nodes()]

    nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color = values, node_size=50, with_labels=False)    
    
    #nx.draw_spring(M, node_size=50, with_labels=False)
    plt.savefig('c-kl11')