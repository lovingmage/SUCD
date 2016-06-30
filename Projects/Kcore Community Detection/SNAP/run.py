import os
import sys

for i in range(2, 44, 2):
	IT = '%d'%i
	command = 'python kcore_commu.py ' + sys.argv[1] + ' ' + IT
	os.system(command)

