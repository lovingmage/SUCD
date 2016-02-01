#!/bin/bash
# run both commu.py(without kcore) and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt") and communities detected

(time python commu.py ../Dataset/netscience.txt > data_netscience.txt) >> result_netscience_nmi_time.txt 2>&1
(time python kcore_commu.py ../Dataset/netscience.txt 0 >data_netscience_kcore0.txt) >> result_netscience_nmi_time.txt 2>&1
(time python kcore_commu.py ../Dataset/netscience.txt 1 >data_netscience_kcore1.txt) >> result_netscience_nmi_time.txt 2>&1
(time python kcore_commu.py ../Dataset/netscience.txt 2 >data_netscience_kcore2.txt) >> result_netscience_nmi_time.txt 2>&1
(time python kcore_commu.py ../Dataset/netscience.txt 3 >data_netscience_kcore3.txt) >> result_netscience_nmi_time.txt 2>&1


# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_netscience.txt data_netscience_kcore0.txt >> result_netscience_nmi_time.txt
python similarity.py data_netscience.txt data_netscience_kcore1.txt >> result_netscience_nmi_time.txt
python similarity.py data_netscience.txt data_netscience_kcore2.txt >> result_netscience_nmi_time.txt
python similarity.py data_netscience.txt data_netscience_kcore3.txt >> result_netscience_nmi_time.txt
