import sys
from sklearn.metrics.cluster import normalized_mutual_info_score
import collections


def main():
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	c_true = {}
	c_pred = {}
	#read data from file
	with open(file1) as fd1, open(file2) as fd2:
		c_true = eval(fd1.readline())
		c_pred = eval(fd2.readline())
	
	#order the data in dictionary data structure
	c_true_order = collections.OrderedDict(sorted(c_true.items()))
	c_pred_order = collections.OrderedDict(sorted(c_pred.items()))
	c_true_label = []
	c_pred_label = []
	
	#make list with community label 
	for k, v in c_true_order.items():
		c_true_label.append(v)
	for k, v in c_pred_order.items():
		c_pred_label.append(v)
	
	print normalized_mutual_info_score(c_true_label,c_pred_label)

if __name__ == "__main__":main()
