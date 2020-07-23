import sys
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

# def swap(s1,s2):
#     swap1=s1
#     s1=s2
#     s2=swap
#     return s1,s2

# Input
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
A1=A
B1=B
A2=A
B2=B


C=[]
count=0
ans=A[N-1]+B[N-1]
ans1=0
ans2=0
swap=0
for i in range(K):
    if(A[0]>B[N-1] or B[0]>A[N-1]):
        ans=A[N-1]+B[N-1]
        print ans
        sys.exit()

for i in range(K):
    # B1[0],A1[N-1] = swap(B1[0],A1[N-1])
    # swap(B1[0],A1[N-1])
    swap=B1[0]
    B1[0]=A1[N-1]
    A1[N-1]=swap
    A1=mergesort(A1)
    B1=mergesort(B1)

ans1=A1[N-1]+B1[N-1]

for i in range(K):
    # A2[0],B2[N-1]=swap(A2[0],B2[N-1])
    # swap(A2[0],B2[N-1])
    swap=A2[0]
    A2[0]=B2[N-1]
    B2[N-1]=swap
    A2=mergesort(A2)
    B2=mergesort(B2)
ans2=A2[N-1]+B2[N-1]

C.append(ans)
C.append(ans1)
C.append(ans2)
C=mergesort(C)

print C[0]
