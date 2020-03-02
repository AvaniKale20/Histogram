import matplotlib.pyplot as plt
# from pylab import *

# only need here one - d array , and y axis contain frequency , no need to write name ..
bloodSuger=[113,85,90,150,149,88,93,115,135,80,77,82,129]

# print(plt.hist(bloodSuger))

# by default it will print 10 bin for you, the concept of bin and bucket is nothing but range
# array([ 77. ,  84.3,  91.6,  98.9, 106.2, 113.5, 120.8, 128.1, 135.4,
#        142.7, 150. ]), this are bins
#array([3., 3., 1., 0., 1., 1., 0., 2., 0., 2.]) this are the y axis array
print()
# we can change the range for three category explicitly, 80 to 100 is normal, 100 to 125 is prediabetic, and to 200 diabetic
# rwidth is relative width of bar compair to bin size
ss=plt.hist(bloodSuger,bins=[80,100,125,200],rwidth=0.95,color='g')
print(ss)


plt.show()