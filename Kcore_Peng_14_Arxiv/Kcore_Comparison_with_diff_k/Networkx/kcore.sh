#!/bin/bash
# run both commu.py(without kcore) and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt") and communities detected

(time python commu.py 3 ../Dataset/dolphin.txt > data_dolphin.txt) >> result_dolphin_nmi_time.txt 2>&1
(time python kcore_commu.py 0 ../Dataset/dolphin.txt >data_dolphin_kcore0.txt) >> result_dolphin_nmi_time.txt 2>&1
(time python kcore_commu.py 1 ../Dataset/dolphin.txt >data_dolphin_kcore1.txt) >> result_dolphin_nmi_time.txt 2>&1
(time python kcore_commu.py 2 ../Dataset/dolphin.txt >data_dolphin_kcore2.txt) >> result_dolphin_nmi_time.txt 2>&1
(time python kcore_commu.py 3 ../Dataset/dolphin.txt >data_dolphin_kcore3.txt) >> result_dolphin_nmi_time.txt 2>&1


# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_dolphin.txt data_dolphin_kcore0.txt >> result_dolphin_nmi_time.txt
python similarity.py data_dolphin.txt data_dolphin_kcore1.txt >> result_dolphin_nmi_time.txt
python similarity.py data_dolphin.txt data_dolphin_kcore2.txt >> result_dolphin_nmi_time.txt
python similarity.py data_dolphin.txt data_dolphin_kcore3.txt >> result_dolphin_nmi_time.txt
