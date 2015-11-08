import community
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Read Network files as gml file type, create a networkx graph and use the eisted graph file
#Random graph may have poor performance, erdos renyi graph doesn't have true community structure
H = nx.read_gml('netscience.gml')
H = nx.k_core (H,2)
#Compute the best partition by using louvain method
partition = community.best_partition(H)

#Plot the result
values = [partition.get(node) for node in H.nodes()]
print H.number_of_nodes()

nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.savefig('netscienceKcore2')
