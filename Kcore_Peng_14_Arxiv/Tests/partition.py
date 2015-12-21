import community
import networkx as nx
import time

print time.time()
G = nx.read_edgelist('facebook_combined.txt')
print time.time()
partition = community.best_partition(G)
print time.time()