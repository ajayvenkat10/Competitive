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

N= int(raw_input(""))
n=raw_input("")
n=n.split(" ")
A=[]

for i in range(N):
    A.append(int(n[i]))

A=mergesort(A)

sum1=0
for i in range(len(A)-1):
    sum1= sum1 + (A[i]*A[i+1])

print sum1
