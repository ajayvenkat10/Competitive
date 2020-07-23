def mergesort(A):
    if(len(A)==1 or len(A)==0):
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

n=int(raw_input(""))
if(n==0):
    print 0
    quit()
A=[]
for i in range(n):
    dimension=raw_input("")
    dimension=dimension.split(" ")
    l = int(dimension[0])
    b = int(dimension[1])
    if(l>b):
        A.append(b)
    else:
        A.append(l)

A=mergesort(A)
A[0]=1
for i in range(len(A)-1):
    if(A[i+1]==A[i]):
        continue
    else:
        A[i+1] = A[i]+1
print A[n-1]
