#!/bin/bash
# run both commu.py(without kcore) and k-core_commu.py with different k-value to get the correspondingrunning time(write into file"result_*_nmi_time.txt") and communities detected

(time python commu.py ../../Datasets/com-amazon.ungraph.txt > data_com-amazon.ungraph.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 1 >data_com-amazon.ungraph_kcore1.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 2 >data_com-amazon.ungraph_kcore2.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 3 >data_com-amazon.ungraph_kcore3.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 4 >data_com-amazon.ungraph_kcore4.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 5 >data_com-amazon.ungraph_kcore5.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 6 >data_com-amazon.ungraph_kcore6.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 7 >data_com-amazon.ungraph_kcore7.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 8 >data_com-amazon.ungraph_kcore8.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 9 >data_com-amazon.ungraph_kcore9.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 10 >data_com-amazon.ungraph_kcore10.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 11 >data_com-amazon.ungraph_kcore11.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 12 >data_com-amazon.ungraph_kcore12.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 13 >data_com-amazon.ungraph_kcore13.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 14 >data_com-amazon.ungraph_kcore14.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 15 >data_com-amazon.ungraph_kcore15.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 16 >data_com-amazon.ungraph_kcore16.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 17 >data_com-amazon.ungraph_kcore17.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 18 >data_com-amazon.ungraph_kcore18.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 19 >data_com-amazon.ungraph_kcore19.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 20 >data_com-amazon.ungraph_kcore20.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 21 >data_com-amazon.ungraph_kcore21.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 22 >data_com-amazon.ungraph_kcore22.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 23 >data_com-amazon.ungraph_kcore23.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 24 >data_com-amazon.ungraph_kcore24.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 25 >data_com-amazon.ungraph_kcore25.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 26 >data_com-amazon.ungraph_kcore26.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 27 >data_com-amazon.ungraph_kcore27.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1
#(time python kcore_commu.py ../../Datasets/com-amazon.ungraph.txt 28 >data_com-amazon.ungraph_kcore28.txt) >> result_com-amazon.ungraph_nmi_time.txt 2>&1


# run similarity.py to get simialities between the communities detected without k-core and communities with differnt k-values 
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore1.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore2.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore3.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore4.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore5.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore6.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore7.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore8.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore9.txt >> result_com-amazon.ungraph_nmi_time.txt
python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore10.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore11.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore12.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore13.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore14.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore15.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore16.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore17.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore18.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore19.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore20.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore21.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore32.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore23.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore24.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore25.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore26.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore27.txt >> result_com-amazon.ungraph_nmi_time.txt
#python similarity.py data_com-amazon.ungraph.txt data_com-amazon.ungraph_kcore28.txt >> result_com-amazon.ungraph_nmi_time.txt
