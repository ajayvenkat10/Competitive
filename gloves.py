import numpy as np

# def mergesort(A):
#     if(len(A)==1 or len(A)==0):
#         return A
#     arr1= mergesort(A[0:len(A)/2])
#     arr2= mergesort(A[len(A)/2:])
#     return merge(arr1,arr2)
#
# def merge(a,b):
#     i=0
#     j=0
#     O=[]
#     while(i<len(a) and j<len(b)):
#         if(a[i]<b[j]):
#             O.append(a[i])
#             i=i+1
#         else:
#             O.append(b[j])
#             j=j+1
#     if(i==len(a)):
#         O.extend(b[j:])
#     else:
#         O.extend(a[i:])
#     return O

n=int(raw_input(""))
A=[]
B=[]
X=[]
for i in range(n):
    A=[]
    B=[]
    a=int(raw_input(""))
    b= raw_input("")
    b=b.split(" ")
    for i in range(a):
        A.append(int(b[i]))

    c= raw_input("")
    c=c.split(" ")
    for i in range(a):
        B.append(int(c[i]))

    C=np.array(A)
    D=np.array(B)

    if((C<=D).all()):
        if((C<=D[::-1]).all()):
            X.append("both")
        else:
            X.append("front")
    elif((C<=D[::-1]).all()):
        X.append("back")
    else:
        X.append("none")

for i in range(len(X)):
    print(X[i])
