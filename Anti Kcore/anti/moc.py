import sys

fd = open(sys.argv[1])
dic = {}
for j in range(0, 242, 1):
	dic[j] = 0
	
#print dic
	
for i in fd.readlines():
	list = []
	list = i.strip().split(' ')
	dic[int(list[1])] = list[0]
	
for key in dic:
	print dic[key]
	
