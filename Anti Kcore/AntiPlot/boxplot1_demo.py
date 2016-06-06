import matplotlib.pyplot as plt
import numpy as np

d1=[0.506666667,0.404428904,0.223529412,0,0.00166113,0.403899721]
d2=[0.506666667,0.404428904,0.223529412,0,0.00166113,0.403899721]
d3=[0.506666667,0.404428904,0.223529412,0,0.257475083,0.403899721]
d4=[0.751111111,0.805361305,0.705882353,0,0.257475083,0.662952646]
d5=[0.751111111,0.805361305,0.705882353,0,0.257475083,0.662952646]
d6=[0.751111111,0.805361305,0.705882353,0,0.257475083,0.662952646]
d7=[0.751111111,0.805361305,0.705882353,0,0.709302326,0.662952646]
d8=[0.822222222,0.864801865,0.779411765,0,0.772425249,0.763231198]
d9=[0.928888889,0.954545455,0.911764706,0.75,0.915282392,0.913649025]
d10=[1,1,1,1,1,1]

data_a=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]

k1=[0.506666667,0.404428904,0.223529412,0,0.00166113,0.403899721]
k2=[0.506666667,0.404428904,0.223529412,0,0.00166113,0.403899721]
k3=[0.537777778,0.48951049,0.255882353,0,0.00166113,0.451253482]
k4=[0.64,0.564102564,0.388235294,0,0.00166113,0.562674095]
k5=[0.764444444,0.715617716,0.502941176,0,0.00166113,0.657381616]
k6=[0.866666667,0.827505828,0.643137255,0,0.003322259,0.771587744]
k7=[0.902222222,0.882284382,0.699019608,0,0.352159468,0.788300836]
k8=[0.946666667,0.938228438,0.780392157,0,0.604651163,0.830083565]
k9=[0.955555556,0.967365967,0.864705882,0,0.850498339,0.896935933]
k10=[1,1,1,1,1,1]

data_b = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10]

ticks = ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

boxprops = dict(linewidth=2)
medianprops1 = dict( linewidth=1.5)
medianprops2 = dict( linewidth=1.5)

meanpointprops = dict(markeredgecolor='black',
                      markerfacecolor='black')

bpl = plt.boxplot(data_a, positions=np.array(xrange(len(data_a)))*2.0-0.4, sym='', widths=0.5, bootstrap=1000, showmeans=True, boxprops=boxprops, medianprops=medianprops1 )
bpr = plt.boxplot(data_b, positions=np.array(xrange(len(data_b)))*2.0+0.4, sym='', widths=0.5, bootstrap=1000, showmeans=True, boxprops=boxprops, medianprops=medianprops2, meanprops = meanpointprops)
set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#000000')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='ResiCore Algorithm')
plt.plot([], c='#000000', label='Kcore Algorithm')
plt.legend()

plt.xticks(xrange(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim((-0.2, 1.3))
#plt.tight_layout()
plt.grid(True)
plt.show()

'''
d1=[0,0,0,0.448979592,0,0,0,0.576271186,0,0,0,0]
d2=[0.424242424,0,0,0.448979592,0.285714286,0.228915663,0,0.576271186,0,0,0,0]
d3=[0.787878788,0.252873563,0.21686747,0.448979592,0.285714286,0.445783133,0,0.576271186,0,0,0,0]
d4=[0.787878788,0.367816092,0.228915663,0.653061224,0.285714286,0.445783133,0,0.576271186,0,0.454545455,0,0.727272727]
d5=[0.787878788,0.436781609,0.590361446,0.653061224,0.387755102,0.469879518,0,0.576271186,0.727272727,0.454545455,0.428571429,0.727272727]
d6=[0.787878788,0.471264368,0.614457831,0.653061224,0.551020408,0.638554217,0,0.779661017,0.727272727,0.727272727,0.785714286,0.727272727]
d7=[0.939393939,0.862068966,0.831325301,0.795918367,0.775510204,0.879518072,1,0.915254237,0.727272727,0.818181818,0.785714286,0.909090909]
d8=[0.939393939,0.862068966,0.831325301,0.795918367,0.775510204,0.879518072,1,0.915254237,0.727272727,0.818181818,0.785714286,0.909090909]
d9=[1,1,1,1,1,1,1,1,1,1,1,1]
d10=[1,1,1,1,1,1,1,1,1,1,1,1]

data=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]

labels = list('ABCD')
fs = 10  # fontsize

boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12,
                  linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black',
                      markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

# demonstrate how to toggle the display of different elements:
plt.boxplot(data, bootstrap=1000, showmeans=True)
plt.grid(True)
plt.ylim((-0.2, 1.3))
plt.show()
'''