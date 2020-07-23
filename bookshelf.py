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
K1=K
for i in range(2,N+2):
    a=int(n[i])
    A.append(a)

for i in range(N+2,len(n)):
    b=int(n[i])
    B.append(b)

A.sort()
B.sort()
A1=A
B1=A
swap=0
# print A
# print A1
# print B
# print B1
while(K!=0):
    # A[0],B[N-1]=swap(A[0],B[N-1])
    swap1=A[0]
    A[0]=B[N-1]
    B[N-1]=swap1
    A.sort()
    B.sort()
    K=K-1

ans=A[N-1]+B[N-1]

while(K1!=0):
    # B1[0],A1[N-1]=swap(B1[0],A1[N-1])
    swap1=B1[0]
    B1[0]=A1[N-1]
    A1[N-1]=swap1
    A1=A1.sort()
    B1=B1.sort()
    K1=K1-1

ans1=A1[N-1]+B1[N-1]

if(ans<ans1):
    print ans

else:
    print ans1
