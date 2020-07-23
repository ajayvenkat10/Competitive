# a=[1,2,3,4]
# b=[4,3,1,4]

# for i in range(len(a)):
    # if(a[i]<=b[i]):
        # count=1
        # else:
        # count=0
        # break

# print count
import numpy as np
a=[1,2,3,4]
b=[4,3,2,4]

A=np.array(a)
B=np.array(b)
if((A<=B[::-1]).all()):
    print ("Success")
