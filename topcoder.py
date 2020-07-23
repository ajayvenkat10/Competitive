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

s=raw_input("")
s=mergesort(s)
print s
c=len(s)
A=[]
i=0
j=0
for i in range(c):
    if(i==0):
        A.append(1)
    elif(s[i]==s[i-1]):
        j=j+1
        A[len(A)-1]=A[len(A)-1]+1
    else:
        j=0
        A.append(1)

A=mergesort(A)
b=len(A)
print A

if(len(A)==1):
    print A[0]**2
else:
    A[b-2]=A[b-1]+A[b-2]
    sum=0
    for i in range(len(A)-1):
        sum=sum+A[i]**2
    print sum
