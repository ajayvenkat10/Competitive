n=int(raw_input(""))
Z=[]
for i in range(n):
    A=[]
    b=raw_input("")
    b=b.split()
    N=int(b[0])
    K=int(b[1])

    x=raw_input("")
    x=x.split()
    for i in range(N):
        A.append(int(x[i]))

    A.sort()
    sum=0
    i=0
    while(i+K-1<N):
        if(A[i]==A[i+(K-1)]):
            if(i+K<N):
                if(A[i]!=A[i+K]):
                    sum=sum+A[i]
                i=i+K
            else:
                i=i+K
        else:
            i=i+1

    if(sum==0):
        Z.append(-1)
    else:
        Z.append(sum)

for i in range(len(Z)):
    print Z[i]
