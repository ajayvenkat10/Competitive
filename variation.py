def mergesort(A):
    if(len(A)==1):
        return A
    arr1= mergesort(A[0:len(A)/2])
    arr2= mergesort(A[len(A)/2:])
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

for i in range(1):
    part=raw_input("")
    part=part.split(" ")
    N=int(part[0])
    K=int(part[1])

n=raw_input("")
n=n.split(" ")
A=[]
for i in range(N):
    a=int(n[i])
    A.append(a)

A=mergesort(A)
# print A
sum1=0
mid=0
for i in range(len(A)):
    low=i
    high=len(A)-1
    # mid=int(low+high)/2
    while low<high:
        mid=int((low+high)/2)
        # print mid
        if(A[mid]-A[i]>=K):
            high=mid
        else:
            low=mid+1
    sum1=sum1+(len(A)-low)
    if(A[low]-A[i] < K):
        sum1 = sum1 - 1
print sum1
