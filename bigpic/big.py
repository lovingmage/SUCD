import sys
import kcore_commu as kc
import jaccard as ja
import time

k0=int(sys.argv[2])
k1=int(sys.argv[3])
filename=sys.argv[1]
dic={}
time1=time.time()
c_true=kc.detect_recover(filename,0)
time2=time.time()
dic[0]=[time2-time1,1]
f=open("out.txt",'w')
f.write("0"+"  "+str(dic[0][0])+"\n")
for i in range(k0,k1+1):
    time1=time.time()
    c_pred=kc.detect_recover(filename,i)
    time2=time.time()
    simi=ja.jaccard_similarity_coefficient(c_true,c_pred)
    dic[i]=[time2-time1,simi]
    f.write(str(i)+"  "+str(dic[i][0])+"  "+str(dic[i][1])+"\n")

