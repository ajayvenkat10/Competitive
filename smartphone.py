n=int(raw_input(""))
A=[]
C=[]
sum=0
for i in range(n):
    a=long(raw_input(""))
    A.append(a)

for i in range(n):
    sum=0
    for j in range(n):
        if(A[i]<=A[j]):
            sum+=A[i]
    C.append(sum)

C.sort()
print C[len(C)-1]
