import networkx as nx
import scipy

G = nx.read_edgelist('./Dataset/enron.txt')

for niter in G.nodes():
    if G.degree(niter) == 1:
        neibor = G.neighbors(niter)[0]
        G.remove_edge(niter, neibor)

out = nx.adjacency_matrix(G)
scipy.io.savemat('enron_Reduce01.mat', mdict={'out': out})
