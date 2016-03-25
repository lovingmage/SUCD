#!/bin/bash
# run both commu.py(without kcore and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt" and communities detected

python commu.py ../../Datasets/twitter_combined.txt > data_twitter_combined.txt
python kcore_commu.py ../../Datasets/twitter_combined.txt 1 >data_twitter_combined_kcore1.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 2 >data_twitter_combined_kcore2.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 3 >data_twitter_combined_kcore3.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 4 >data_twitter_combined_kcore4.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 5 >data_twitter_combined_kcore5.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 6 >data_twitter_combined_kcore6.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 7 >data_twitter_combined_kcore7.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 8 >data_twitter_combined_kcore8.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 9 >data_twitter_combined_kcore9.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 10 >data_twitter_combined_kcore10.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 11 >data_twitter_combined_kcore11.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 12 >data_twitter_combined_kcore12.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 13 >data_twitter_combined_kcore13.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 14 >data_twitter_combined_kcore14.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 15 >data_twitter_combined_kcore15.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 16 >data_twitter_combined_kcore16.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 17 >data_twitter_combined_kcore17.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 18 >data_twitter_combined_kcore18.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 19 >data_twitter_combined_kcore19.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 20 >data_twitter_combined_kcore20.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 21 >data_twitter_combined_kcore21.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 22 >data_twitter_combined_kcore22.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 23 >data_twitter_combined_kcore23.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 24 >data_twitter_combined_kcore24.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 25 >data_twitter_combined_kcore25.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 26 >data_twitter_combined_kcore26.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 27 >data_twitter_combined_kcore27.txt 
python kcore_commu.py ../../Datasets/twitter_combined.txt 28 >data_twitter_combined_kcore28.txt 


# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore1.txt ../../Datasets/twitter_combined.txt 1
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore2.txt ../../Datasets/twitter_combined.txt 2
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore3.txt ../../Datasets/twitter_combined.txt 3
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore4.txt ../../Datasets/twitter_combined.txt 4
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore5.txt ../../Datasets/twitter_combined.txt 5
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore6.txt ../../Datasets/twitter_combined.txt 6
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore7.txt ../../Datasets/twitter_combined.txt 7
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore8.txt ../../Datasets/twitter_combined.txt 8
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore9.txt ../../Datasets/twitter_combined.txt 9
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore10.txt ../../Datasets/twitter_combined.txt 10
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore11.txt ../../Datasets/twitter_combined.txt 11
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore12.txt ../../Datasets/twitter_combined.txt 12
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore13.txt ../../Datasets/twitter_combined.txt 13
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore14.txt ../../Datasets/twitter_combined.txt 14
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore15.txt ../../Datasets/twitter_combined.txt 15
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore16.txt ../../Datasets/twitter_combined.txt 16
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore17.txt ../../Datasets/twitter_combined.txt 17
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore18.txt ../../Datasets/twitter_combined.txt 18
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore19.txt ../../Datasets/twitter_combined.txt 19
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore20.txt ../../Datasets/twitter_combined.txt 20
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore21.txt ../../Datasets/twitter_combined.txt 21
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore22.txt ../../Datasets/twitter_combined.txt 22
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore23.txt ../../Datasets/twitter_combined.txt 23
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore24.txt ../../Datasets/twitter_combined.txt 24
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore25.txt ../../Datasets/twitter_combined.txt 25
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore26.txt ../../Datasets/twitter_combined.txt 26
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore27.txt ../../Datasets/twitter_combined.txt 27
python similarity.py data_twitter_combined.txt data_twitter_combined_kcore28.txt ../../Datasets/twitter_combined.txt 28
