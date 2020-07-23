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

def swap(s1,s2):
    return s2,s1

n=raw_input("")
n=n.split()
N=int(n[0])
K=int(n[1])
A=[]
B=[]

for i in range(2,N+2):
    a=int(n[i])
    A.append(a)

for i in range(N+2,len(n)):
    b=int(n[i])
    B.append(b)

A=mergesort(A)
B=mergesort(B)

ans= A[N-1]+B[N-1]
ans1=0

for i in range(K):
    if(A[0]>B[N-1] or B[0]>A[N-1]):
        ans=A[N-1]+B[N-1]
        break
    else:
        if(A[N-1]>B[N-1]):
            if(A[N-2]<B[N-2]):
                A[N-1],B[0]=swap(A[N-1],B[0])
            else:
                A[0],B[N-1]=swap(A[0],B[N-1])

        elif(A[N-1]==B[N-1]):
            if(A[N-2]== B[N-2]):
                A[N-1],B[0]=swap(A[N-1],B[0])

            elif(A[N-2]>B[N-2]):
                A[0],B[N-1]=swap(A[0],B[N-1])

            else:
                B[0],A[N-1]=swap(B[0],A[N-1])
        else:
            if(B[N-2]<A[N-2]):
                B[N-1],A[0]=swap(B[N-1],A[0])
            else:
                B[0],A[N-1]=swap(B[0],A[N-1])

        A=mergesort(A)
        B= mergesort(B)
        ans1= A[N-1]+B[N-1]
        if(ans1<ans):
            ans=ans1

print ans
