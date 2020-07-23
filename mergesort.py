def mergesort(A):
    if(len(A)==1):
        return A
    arr1= mergesort(A[0:int(len(A)/2)])
    arr2= mergesort(A[int(len(A)/2):])
    return merge(arr1,arr2)

def merge(a,b):
    i=0
    j=0
    O=[]
    while(i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            O.append(a[i])
            i=i+1
        else:
            O.append(b[j])
            j=j+1
    if(i==len(a)):
        O.extend(b[j:])
    else:
        O.extend(a[i:])
    return O

A=[]
n=int(input(""))
for i in range(n):
    b = int(input(""))
    A.append(b)
A=mergesort(A)
print(A)
