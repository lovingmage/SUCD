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

#This function is used to create the node vector called NodeV of a given graph
def create_node_vector(G):
	"""Create Node Vectors by extracting given graph G .
    Parameters
    ----------
    G : snap graph
    source : node, optional
       
    Returns
    -------
    NodeV: TIntV
       A TIntV vector which store all node ids of the given graph.
    Examples
    --------
    >>> NodeV_G = create_node_vector(G)
    >>> print NodeV_G
    <snap.TIntV; proxy of <Swig Object of type 'TVec< TInt > *' at 0x108fa8ea0> >
    Notes
    -----
    by C. Wang, Jan 16.
    This code is used for convenient computing, for instance, we may use the 
    intersection function of Vector structure when we want to recover Kcore
    partition into original partition.
    """
	NodeV = snap.TIntV()
	for node in G.Nodes():
		NodeV.Add(node.GetId())
	#print NodeV[200]
	return NodeV


def get_diff_from_kcore(NodeV_G,NodeV_Kcore):
	"""This function is used to calculate the nodes set which are not in Kcore.
	   Which are the missing nodes when we apply kcore based community detection.

    Parameters
    ----------
    NodeV_G : Node Vector of original graph G, type TIntV
    NodeV_Kcore : Node Vector of Kcore subgraph Kcore, type TIntV
       
    Returns
    -------
    NodeV_Diff: TIntV
       A TIntV vector which store all node ids which appears in G but not in Kcore.

    Examples
    --------
    >>> NodeV_Diff = get_diff_from_kcore(NodeV_G, NodeV_Kcore)
    >>> print NodeV_Diff
    <snap.TIntV; proxy of <Swig Object of type 'TVec< TInt > *' at 0x108fa8ea0> >
    Notes
    -----
    by C. Wang, Jan 16.
    """
	NodeV_Diff = snap.TIntV()
	NodeV_G.Diff(NodeV_Kcore, NodeV_Diff)
	#print NodeV_Diff[0]
	return NodeV_Diff


def sort_by_neighbor(NodeV_Diff, Kcore, G):
	SortH = snap.TIntIntH()

	for node in NodeV_Diff:
		SortH[node] = 0
		for neighbor in G.GetNI(node).GetOutEdges():
			if Kcore.IsNode(neighbor):
				SortH[node] += 1
	SortH.Sort(False, True)
	#SortedV = snap.TIntV()
	#for key in temp_hash_table:
	#	SortedV.Add(key)
	return SortH


def community_partition(G):
	CommuV = snap.TCnComV()
	modularity = snap.CommunityCNM(G, CommuV)
	ComutyH = snap.TIntIntH()
	partition = 0
	for community in CommuV:
		for NI in community:
			ComutyH[NI] = partition
		partition = partition + 1
	return ComutyH



def recover_partition_by_kcore(Partition_KcoreH, SortH, G):
	Recover_PartitionH = snap.TIntIntH()
	Recover_PartitionH = Partition_KcoreH

	i = 0
	for node in SortH:
		if SortH[node] == 0:
			Recover_PartitionH[node] = i - 1
		else :
			Recover_PartitionH[node] = vote_for_node(node, Partition_KcoreH, G, Kcore)
	return Recover_PartitionH



def vote_for_node(node, PartitionH, G, Kcore):
	VoteNodeH = snap.TIntIntH()
	for neighbor in G.GetNI(node).GetOutEdges():
		if Kcore.IsNode(neighbor):
			key = PartitionH[neighbor]
			if VoteNodeH.IsKey(key):
				VoteNodeH[key] += 1
			else:
				VoteNodeH[key] = 1 
	VoteNodeH.Sort(False, True)
	return VoteNodeH.GetKey(0)



	


if __name__ == '__main__':

	G = snap.LoadEdgeList(snap.PUNGraph, "facebook_combined.txt", 0, 1)
	
	NodeV_G = create_node_vector(G)
	print NodeV_G
	Kcore = snap.GetKCore(G, 5)
	NodeV_Kcore = create_node_vector(Kcore)
	NodeV_Diff = get_diff_from_kcore(NodeV_G, NodeV_Kcore)

	SortH = sort_by_neighbor(NodeV_Diff, Kcore, G)
	Partition_KcoreH = community_partition(Kcore)
	Partition_RecoverH = recover_partition_by_kcore(Partition_KcoreH, SortH, G)


	#Start Community Detection on Kcore Subgraph
	#partition = snap.TInt(0)
	#partition.Val = partition.Val + 2
	#print partition.Val

	


	

	#p2 = time.time()
	#print p2 - p1
	#SKCore.Dump()
	#Start log file, create log file and start.
