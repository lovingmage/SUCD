import community
import sys
import networkx as nx


G = nx.read_gml('soc-google-plus.gml')
partition = community.best_partition(G)
print partition
