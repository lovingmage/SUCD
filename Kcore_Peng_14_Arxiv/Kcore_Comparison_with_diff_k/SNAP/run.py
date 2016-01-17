import os
import sys

for i in range(1, 1500, 1):
	IT = '%d'%i
	command = 'python kcore_commu.py ' + sys.argv[1] + ' ' + IT
	os.system(command)

