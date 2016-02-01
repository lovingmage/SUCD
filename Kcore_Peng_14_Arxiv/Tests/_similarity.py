import sys
from sklearn.metrics.cluster import normalized_mutual_info_score

def nimSimilarity(c_true, c_pred):
	'''This will return the Normalized Mutual Information between two clusterings
	 Parameters:     c_true, communities detected without kcore, a dictionary with community node as the key and community lable as the value
			 c_pred, communities detected with kcore, a dictionary with community node as the key and community lable as the value
	Return nmi

	Example:
	x = {1:1,2:1,3:0,4:0}
	y = {1:0,2:0,3:1,4:1}

	print nimSimilarity(x,y)'''

	#put community lables (lable might be duplicate)into array
	c_true = list(c_true.values())
	#print sorted(c_true)
	c_pred = list(c_pred.values())
	#print sorted(c_pred)
	return normalized_mutual_info_score(c_true,c_pred)



def main():
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	c_true = {}
	c_pred = {}
	with open(file1) as fd1, open(file2) as fd2:
		c_true = eval(fd1.readline())
		c_pred = eval(fd2.readline())
		
	print nimSimilarity(c_true, c_pred)

if __name__ == "__main__":main()
