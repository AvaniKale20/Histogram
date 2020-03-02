import matplotlib.pyplot as plt
# from pylab import *
# how to print bar graph side by side...

bloodSugerForMen=[99,45,100,112,234,123,128,90,178,101,77,87,50]
bloodSugerWomen=[113,85,90,150,149,88,93,115,135,80,77,82,129]
print()
ss=plt.hist([bloodSugerForMen,bloodSugerWomen],bins=[80,100,125,200],rwidth=0.95,color=['green','orange'],label=['men','women'])
print(ss)

plt.xlabel("sugar range")
plt.ylabel("number of patient")
plt.title("blood suger analysis")
plt.legend()

plt.show()
