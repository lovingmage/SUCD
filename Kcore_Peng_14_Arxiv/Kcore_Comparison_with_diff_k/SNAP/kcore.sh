#!/bin/bash
# run both commu.py(without kcore) and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt") and communities detected
#rm data_* result* LOG*
(time python commu.py Dataset/ca-AstroPh.txt > data_ca-AstroPh.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1

(time python kcore_commu.py Dataset/ca-AstroPh.txt 0 >data_ca-AstroPh_kcore0.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1
(time python kcore_commu.py Dataset/ca-AstroPh.txt 4 >data_ca-AstroPh_kcore4.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1
(time python kcore_commu.py Dataset/ca-AstroPh.txt 6 >data_ca-AstroPh_kcore6.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1
(time python kcore_commu.py Dataset/ca-AstroPh.txt 8 >data_ca-AstroPh_kcore8.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1

#(time python kcore_commu.py Dataset/ca-AstroPh.txt 6 >data_ca-AstroPh_kcore5.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1
#(time python kcore_commu.py Dataset/ca-AstroPh.txt 8 >data_ca-AstroPh_kcore6.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1
#(time python kcore_commu.py Dataset/ca-AstroPh.txt 9 >data_ca-AstroPh_kcore7.txt) >> result_ca-AstroPh_nmi_time.txt 2>&1

# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore0.txt >> result_ca-AstroPh_nmi_time.txt
python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore4.txt >> result_ca-AstroPh_nmi_time.txt
python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore6.txt >> result_ca-AstroPh_nmi_time.txt
python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore8.txt >> result_ca-AstroPh_nmi_time.txt
#python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore6.txt >> result_ca-AstroPh_nmi_time.txt
#python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore8.txt >> result_ca-AstroPh_nmi_time.txt
#python similarity.py data_ca-AstroPh.txt data_ca-AstroPh_kcore9.txt >> result_ca-AstroPh_nmi_time.txt
