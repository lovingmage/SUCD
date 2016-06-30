#!/bin/bash
# run both commu.py(without kcore) and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt") and communities detected
#rm data_* result* LOG*
(time python commu.py Dataset/facebook_combined.txt > data_facebook_combined.txt) >> result_facebook_combined_nmi_time.txt 2>&1

(time python kcore_commu.py Dataset/facebook_combined.txt 0 >data_facebook_combined_kcore0.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(time python kcore_commu.py Dataset/facebook_combined.txt 4 >data_facebook_combined_kcore4.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(time python kcore_commu.py Dataset/facebook_combined.txt 6 >data_facebook_combined_kcore6.txt) >> result_facebook_combined_nmi_time.txt 2>&1
(time python kcore_commu.py Dataset/facebook_combined.txt 8 >data_facebook_combined_kcore8.txt) >> result_facebook_combined_nmi_time.txt 2>&1

#(time python kcore_commu.py Dataset/facebook_combined.txt 6 >data_facebook_combined_kcore5.txt) >> result_facebook_combined_nmi_time.txt 2>&1
#(time python kcore_commu.py Dataset/facebook_combined.txt 8 >data_facebook_combined_kcore6.txt) >> result_facebook_combined_nmi_time.txt 2>&1
#(time python kcore_commu.py Dataset/facebook_combined.txt 9 >data_facebook_combined_kcore7.txt) >> result_facebook_combined_nmi_time.txt 2>&1

# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore0.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore4.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore6.txt >> result_facebook_combined_nmi_time.txt
python similarity.py data_facebook_combined.txt data_facebook_combined_kcore8.txt >> result_facebook_combined_nmi_time.txt
#python similarity.py data_facebook_combined.txt data_facebook_combined_kcore6.txt >> result_facebook_combined_nmi_time.txt
#python similarity.py data_facebook_combined.txt data_facebook_combined_kcore8.txt >> result_facebook_combined_nmi_time.txt
#python similarity.py data_facebook_combined.txt data_facebook_combined_kcore9.txt >> result_facebook_combined_nmi_time.txt
