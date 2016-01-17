import os
for it in range(1, 797, 1):
	IT = '%d' %it
	tem_name = 'LOG_File_facebook_combined.txt' + IT + '.log' 
	f = open(tem_name,'r')  
	f.readline()
	f.readline()
	f.readline()
	f.readline()
	f.readline()

	list = f.readline().split(' ')
	list2 = list[-1]
	print list2[0:-1]
