#!/bin/bash
# run both commu.py(without kcore) and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt") and communities detected

(python commu.py ../../Datasets/facebook_combined.txt > data_facebook_combined.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 1 >data_facebook_combined_kcore1.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 2 >data_facebook_combined_kcore2.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 3 >data_facebook_combined_kcore3.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 4 >data_facebook_combined_kcore4.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 5 >data_facebook_combined_kcore5.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 6 >data_facebook_combined_kcore6.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 7 >data_facebook_combined_kcore7.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 8 >data_facebook_combined_kcore8.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 9 >data_facebook_combined_kcore9.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 10 >data_facebook_combined_kcore10.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 11 >data_facebook_combined_kcore11.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 12 >data_facebook_combined_kcore12.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 13 >data_facebook_combined_kcore13.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 14 >data_facebook_combined_kcore14.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 15 >data_facebook_combined_kcore15.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 16 >data_facebook_combined_kcore16.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 17 >data_facebook_combined_kcore17.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 18 >data_facebook_combined_kcore18.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 19 >data_facebook_combined_kcore19.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 20 >data_facebook_combined_kcore20.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 21 >data_facebook_combined_kcore21.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 22 >data_facebook_combined_kcore22.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 23 >data_facebook_combined_kcore23.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 24 >data_facebook_combined_kcore24.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 25 >data_facebook_combined_kcore25.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 26 >data_facebook_combined_kcore26.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 27 >data_facebook_combined_kcore27.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(python kcore_commu.py ../../Datasets/facebook_combined.txt 28 >data_facebook_combined_kcore28.txt) >> result_facebook_combined_nmi_time.txt 2>&1


# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore1.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore2.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore3.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore4.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore5.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore6.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore7.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore8.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore9.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore10.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore11.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore12.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore13.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore14.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore15.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore16.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore17.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore18.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore19.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore20.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore21.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore22.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore23.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore24.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore25.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore26.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore27.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore28.txt >> result_facebook_combined_nmi_time.txt
