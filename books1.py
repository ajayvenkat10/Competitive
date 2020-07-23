# def mergesort(A):
#     if(len(A)==1):
#         return A
#     arr1= mergesort(A[0:len(A)/2])
#     arr2= mergesort(A[len(A)/2:])
#     return merge(arr1,arr2)
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
def swap(s1,s2):
    return s2,s1
n=raw_input("")
n=n.split()
N=int(n[0])
K=int(n[1])
A=[]
B=[]
C=[]
D=[]
a=0
b=0
for i in range(2,N+2):
    a=int(n[i])
    A.append(a)
    C.append(a)
for k in range((N+2),len(n)):
    b=int(n[k])
    B.append(b)
    D.append(b)
A.sort()
B.sort()
C.sort()
D.sort()
swap=0
swap1=0
ans1=0
ans2=0
for i in range(K):
    swap1=A[0]
    A[0]=B[N-1]
    B[N-1]=swap1
    A.sort()
    B.sort()
#     print A
#     print B
#
# print C
# print D
ans1=A[N-1]+B[N-1]
for i in range(K):
    swap=D[0]
    D[0]=C[N-1]
    C[N-1]=swap
    C.sort()
    D.sort()
    # print C
    # print D
ans2=C[N-1]+D[N-1]
if(ans1<=ans2):
    print ans1
else:
    print ans2
