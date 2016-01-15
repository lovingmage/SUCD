'''
   This code is designed and written by Chenghong Wang.
   Do not copy, disclose, or distribute without explicit written permission. 

   Author: 			Chenghong Wang <cwang132@syr.edu>
   
   Instruction:			This program is a python package which is designed to compute the community
				partition by using kcore method. The kore method is to firstly reduce the
				original graph by using kcore method; Then perform community detection method
				on the searched kcore subgraph, then recover the subgraph and the community
				structure.
					
	Usage:			This is a package of kcore community detection, to use all function here, by
				using :

					In Linux Command Line using the following command
					
					$python kcore_comm.py [INPUT_FILE_TYPE] [Kcore Number]
	
					
'''

import snap
import os
import time

def create_node_vector(G):
	NodeV = snap.TIntV()
	for node in G.Nodes():
		NodeV.Add(node.GetId())
	return NodeV

def get_diff_from_kcore(NodV_G,NodV_Kcore):
	NodeV_G = snap.TIntV()
	NodeV_Kcore = snap.TIntV()
	NodeV_Diff = snap.TIntV()
	NodeV_G.Diff(NodeV_Kcore, NodeV_Diff)
	return NodeV_Diff

def sort_by_neighbor(NodeV_Diff, Kcore, G):
	temp_hash_table = snap.TIntIntH()

	for node in NodeV_Diff:
		temp_hash_table[node] = 0
		for neighbor in G.GetNI(node).GetOutEdges():
			if Kcore.IsNode(neighbor):
				temp_hash_table[node] += 1
	temp_hash_table.Sort(False, True)
	return temp_hash_table



if __name__ == '__main__':

	G = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
	
	NodeVec_G = create_node_vector(G)
	Kcore = snap.GetKCore(G, 5)
	NodeV_Kcore = create_node_vector(Kcore)
	NodeV_Diff = snap.TIntV()
	NodeV_Diff = get_diff_from_kcore(NodeVec_G, NodeV_Kcore)
	Hash = sort_by_neighbor(NodeV_Kcore, Kcore, G)
	#print Hash.GetKey(1)

	

	#p2 = time.time()
	#print p2 - p1
	#SKCore.Dump()
	#Start log file, create log file and start.
