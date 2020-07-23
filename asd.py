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
    while len(A)>0:
        count=0
        x=A[i]
        j=0
        while(A[j]<=x):
            if(x==A[i]):
                count+=1
            j+=1
        A=A[j:]
        if(count==K):
            sum=sum+x


    if(sum==0):
        Z.append(-1)
    else:
        Z.append(sum)

for i in range(len(Z)):
    print Z[i]
