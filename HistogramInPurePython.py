# from collections import Counter
from collections import Counter

from matplotlib.pyplot import hist

a=(0,1,1,1,2,3,7,7,23)
# how many times each value appers , 'countElement()' function we are taking for to calculate' HOW MAnY times EachValue Appers/prsent'
# Ex: 0 :is onkly once, 1 :is appers 3 times...
# count_elements() returns a dictionary with unique elements from the sequence as keys and their frequencies (counts) as values.
# hist is using for plot histogram
def countElement(varA) :

    hist={}
    for i in varA:
        hist[i]=hist.get(i,0)+1
    return hist


counted= countElement(a)
print(counted)

print()
# It is done by collection, We have to import Counter class.
recounter=Counter(a)
print(recounter)

# We can confirm that our handmade function 'countElement(varA)' virtually does the same thing as collection.Counter()
# by testing equally between two .....
print()
print(recounter.items() == counted.items())