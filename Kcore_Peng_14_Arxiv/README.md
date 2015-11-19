## 0x01 Introduction ##
Accelerating Community Detection by Using K-core Subgraphs is proposed by Peng et.al. in Arxiv 2014 [1], and have been proved by the author that it is indeed a good method to boost community detection process. We will try to re-perform the community detection process by using their method.

## 0x02 Environment and Implementation Platform ##
The necessary toolkit and packages required in our implementation are listed as follows.

* Python 2.7.x
* Networkx 1.9.19 (Do not use the latest version.)
* python-louvain
* Matplotlib

Use can firstly install python and using python pip toolkit to install the remain toolkits. Please do not use python 3.3 or above version, and do not install networkx version other than 1.9.19. Please be aware that the Networkx 1.10.x have some bugs remain unsolved.

## 0x03 Get Started ##
Be cool if you have already done the previous works, you can start to play the script now.
Within this files, contains all the code wich can perform k-core community detection works, Peng gave us a method on how to boost up the community detection works on kcore subgraph, and the algorithm can be described as follows:

1. For any given graph G, search the kcore subgraph H.
2. Perform some community detection algorithm on the kcore subgraph H.
3. For each nodes that not in H but in G, we proceed them into recover step.
4. Optimize the total network structure.

## Reference ##

1. Peng, Chengbin, Tamara G. Kolda, and Ali Pinar. "Accelerating community detection by using k-core subgraphs." arXiv preprint arXiv:1403.2226 (2014).
2. Dorogovtsev, Sergey N., Alexander V. Goltsev, and Jose Ferreira F. Mendes. "K-core organization of complex networks." Physical review letters 96.4 (2006): 040601.






