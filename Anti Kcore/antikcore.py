'''
/////////////////////////////////////////////////////////////////////////
// antikcore.py - Python Package for decompose resilience core         //
// ver 1.5                                                             //
// Author : Chenghong Wang                                             //
// Contact: chw336@ucsd.edu                                            //
//---------------------------------------------------------------------//
// Chenghogn Wang (c) copyright 2016                                   //
// All rights granted provided this copyright notice is retained       //
//---------------------------------------------------------------------//
// Application:     sucd - component                                   //
// Platform:    Spyder Python 2.7                                      //
/////////////////////////////////////////////////////////////////////////
/*
*  Package Operations:
*  -------------------
*  Provides four classes that wrap the Winsock API:
*  Socket:
*  - provides all the functionality necessary to handle server clients
*  - created by SocketListener after accepting a request
*  - usually passed to a client handling thread
*  SocketConnecter:
*  - adds the ability to connect to a server
*  SocketListener:
*  - adds the ability to listen for connections on a dedicated thread
*  - instances of this class are the only ones influenced by ipVer().
*    clients will use whatever protocol the server provides.
*  SocketSystem:
*  - Loads and unloads winsock2 library.  
*  - Declared once at beginning of execution
*
*  Required Files:
*  ---------------
*	networkx， matplotlib, community, sys, random
*
*  Maintenance History:
*  --------------------
*  Ver 4.0 : 24 Mar 15
*  - first release of total redesign - had a known bug (see ver 4.1)
*/
/*
* ToDo:
* - make SocketSystem a reference counted instance of Socket
* - write buffered recv which efficiently returns string or line
*   - reads and concatenates everything available into circular buffer
*   - parses out first string or line and moves start of buffer pointer
*     to begining of next
* -----------------------------------------------------------------------
*  Wait for The next items until Students have submitted their code
* -----------------------------------------------------------------------
* - build front end, e.g., Sender and Receiver classes
* - implement message facility: message class, sendMsg and recvMsg
* - Test and Display packages
*/
'''
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import community
import sys
import random


def anti_kcore(G, k = None, core_number = None):
    if core_number is None:
        core_number = nx.core_number(G)
    if k is None:
        k = max(core_number.values())
    nodes = (n for n in core_number if core_number[n] >= k)
    anti_nodes = (n for n in core_number if core_number[n] < k)
    return (G.subgraph(anti_nodes).copy(), list(nodes))
	
 #<-------------Resicore without hard bound------------->
def resi_core(G):
    resi_node = []
    G1 = G
      
    while (len(resi_node) < upper_bound) :
        (H, temp) = anti_kcore(G1)
        G1 = H
        resi_node = resi_node + temp
        
    return G.subgraph(resi_node).copy()
     
     
#<------------ResiCore with Hard Upperbound------------->
def resi_subgraph(G, upper_bound):

    resi_node = []
    G1 = G
      
    while (len(resi_node) < upper_bound) :
        (H, temp) = anti_kcore(G1)
        G1 = H
        curr_size = len(resi_node) + len(temp)
        if (curr_size < upper_bound):
            resi_node = resi_node + temp
            print resi_node
            continue
        else:
		ranPick = int(upper_bound - len(resi_node))
		random.shuffle(temp)
		resi_node = resi_node + temp[0:ranPick]
		break
        

    return G.subgraph(resi_node).copy()
    
    
    
    
#<------------Test Stub------------>
if __name__ == "__main__":
    FILE_PATH = sys.argv[1]
    
    G = nx.read_edgelist(FILE_PATH)
    node_size = int(sys.argv[2])
    '''Set Upper Bound Graph Scale'''
    upper_bound = int(0.1 * node_size * len(G.nodes()))
    
    ## Test The minimal resicore
    #M, l1 = anti_kcore(G)
    #print l1
    

    M = resi_subgraph(G, upper_bound)

    partition = community.best_partition(M)
    for key in partition.keys():
		print key  
    