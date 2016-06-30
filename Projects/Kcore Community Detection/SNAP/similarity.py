import sys
from sklearn.metrics.cluster import normalized_mutual_info_score

'''This will return the Normalized Mutual Information between two clusterings'''



def main():
	c_true = [line.strip() for line in open(sys.argv[1], 'r')]	
	c_pred = [line.strip() for line in open(sys.argv[2], 'r')]	
	print normalized_mutual_info_score(c_pred, c_true)

if __name__ == "__main__":main()
