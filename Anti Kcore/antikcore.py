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
*  Sockets.h, Sockets.cpp, 
*  Logger.h, Logger.cpp, 
*  Utilities.h, Utililties.cpp, 
*  WindowsHelpers.h, WindowsHelpers.cpp
*
*  Maintenance History:
*  --------------------
*  ver 5.1 : 10 Apr 16
*  - Added sendStream and recvStream to support sending and receiving
*    file streams.  These simply wrap the native sockets send and recv.
*  ver 5.0 : 04 Mar 16
*  - Fixed bugs in Socket test stub, essentially stealing fixes from
*    ClientTest.cpp and ServerTest.cpp
*  - Didn't change any code in the Socket library itself
*  ver 4.9 : 04 Mar 16
*  - Added a single write statement in Socket::Listener::accept()
*  ver 4.8 : 22 Feb 16
*  - Replaced verbose I/O with Logger I/O
*  - Replaced ApplicationHelpers package with Utilities package
*  ver 4.7 : 04 Apr 15
*  - removed testBlockHandling declaration from Socket.cpp ClientHandler.
*    The implementation had already been removed, I just forgot the declaration.
*  - added test for INVALID_SOCKET in Socket::recvString.  The omission was
*    reported by Huanming Fang.  Thanks Huanming.
*  ver 4.6 : 30 Mar 15
*  - minor modification to comments, above, and in Socket class implem.
*  ver 4.5 : 30 Mar 15
*  - moved SocketListener::start(...) from cpp to h file since it is a
*    template method.
*  - renamed ClientProc to ClientHandler
*  - removed Block operations to avoid binding Socket package to
*    FileSystem package.  Will add buffer operations to the
*    FileSystem::File class to match the Socket buffer operations.
*  - gave ClientHandler a command interpreter to select a test process
*    - test string tranfers
*    - test buffer transfers
*    - client sends a string to select test mode
*    - test modes are (string, buffer, and stop)
*  - Created a Verbose class in AppHelpers package that locks stream io.
*    That helps to keep server and client io text from intermingling.
*    You can turn verbose mode off which silences output that isn't
*    marked "always".
*  - Fixed again the bug which prevented communicating with anything other
*    than the loopback by adding hints.ai_flags = AI_PASSIVE to
*    SocketListener member data.
*  - added more testing
*  ver 4.4 : 27 Mar 15
*  - minor changes to comments
*  - moved ClientHandler into test stub
*  ver 4.3 : 26 Mar 15
*  - fixed bug noticed by Tarun Rajput 
*  - used '0' as terminator.  Should have been '\0'
*  ver 4.2 : 26 Mar 15
*  - several small changes to the Socket class interface
*  ver 4.1 : 25 Mar 15
*  - fixed connection bug that prevented connecting to anything
*    other than a loopback (localhost, 127.0.0.1, ::1) by
*    adding winsock code to SocketConnecter().
*  - removed low-level code from ClientProc 
*    (server's client handler callable object)
*    replaced with code written to Socket interface
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
     
<<<<<<< HEAD
	
    
if __name__ == "__main__":
    FILE_PATH = sys.argv[1]
    
    G = nx.read_edgelist(FILE_PATH)
    node_size = int(sys.argv[2])
    '''Set Upper Bound Graph Scale'''
    upper_bound = int(0.1 * node_size * len(G.nodes()))
    
    
    M = resi_core(G)
    #nx.draw_spring(G)
    #plt.savefig('origin')
    
    '''
    (H, temp) = anti_kcore(G)
    M = G.subgraph(temp)
    
    nx.draw_spring(M)
    plt.savefig('dl2')
    '''
    
    
=======
     
#<------------ResiCore with Hard Upperbound------------->
def resi_subgraph(G, upper_bound):

>>>>>>> master
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
        

<<<<<<< HEAD
    M = G.subgraph(resi_node).copy()
#    print len(M)

    partition = community.best_partition(M)
    for key in partition.keys():
	print key  
 
    '''outPartition = json.dumps(partition)  
    json.dump(outPartition, open(sys.argv[1]+".dat", 'w'))
=======
    return G.subgraph(resi_node).copy()
>>>>>>> master
    
    
<<<<<<< HEAD
    #nx.draw_spring(M, node_size=50, with_labels=False)
    plt.savefig('c-dl' + sys.argv[1])'''

=======
>>>>>>> master
    
    
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
    