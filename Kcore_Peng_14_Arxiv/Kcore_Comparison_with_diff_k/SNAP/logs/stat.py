import os
for it in range(2, 42, 2):
	IT = '%d' %it
	tem_name = './emali/LOG_File_email-Enron.txt' + IT + '.log' 
	f = open(tem_name,'r')  
	f.readline()
	f.readline()
	f.readline()
	f.readline()
	f.readline()

	list = f.readline().split(' ')
	list2 = list[-1]
	print list2[0:-1]
