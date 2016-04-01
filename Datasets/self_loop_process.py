import sys
if __name__ == '__main__':
	DATA_FILE = sys.argv[1].split("/")
	FILE_NAME = "without_selfloop_" + (DATA_FILE[-1])
	f1 = open(sys.argv[1],'r')
	result = list()
	for line in f1.readlines():
		line.strip()
		if line == '\n':
                        break
		argu  = line.split()
		if (argu[0]!=argu[1]):
			result.append(line)
	f1.close()
	f2 = open(FILE_NAME,'w')
	for line in result:
		f2.write(line)
	f2.close()


