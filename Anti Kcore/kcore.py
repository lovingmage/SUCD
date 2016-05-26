import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    FILE_PATH = "./test.txt"
    G = nx.read_edgelist(FILE_PATH)
    H = nx.k_core(G, 3)
    
        
    nx.draw_spring(H)
    plt.savefig('core-3')