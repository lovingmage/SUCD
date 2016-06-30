## 0x01 Introduction ##

*commu.py* is used to find communities without performing kcore,  plz check if i commented out lines correctly

*kcore.sh*: run commu.py, kcore_commu.py and similarity to get the respective running time and nmi similarity. 

You can do the testing with different dataset by replacing the datafile name with below command in vim (e.g. replacing dolphin with netscience ): %s/dolphin/netscience/g
and the result (totoal running time and nmi similarity will bw written into one file named: result_*_nmi_time.txt) (* is the dataset file name)


you can simply run it as below shows:
./kcore.sh  (if permission issue, plz change the mode first: chmod u+x  kcore.sh)








