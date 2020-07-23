n= int(raw_input(""))
A=[]
C=[]
sum=0
for i in range(n):
    A=[]
    sum=0
    a=int(raw_input(""))
    b=raw_input("")
    b=b.split()
    for i in range(a):
            A.append(int(b[i]))

    for i in range(len(A)):
        sum=sum+A[i]

    if(sum%2==1):
        C.append("YES")

    else:
        C.append("NO")

for i in range(len(C)):
    print C[i]
