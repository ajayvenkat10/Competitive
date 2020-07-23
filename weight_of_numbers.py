t=int(raw_input(""))
Z=[]
for i in range(t):
    a=raw_input("")
    a=a.split()
    N=int(a[0])
    K=int(a[1])
    X=[]

    if(K>=0):
        for i in range(1,10-K):
            m=i
            n=N-1
            sum=0
            count=0
            while(n>=0 and m<=9):
                sum=sum+(m*(10**n))
                n=n-1
                m=m+K
                count=count+1

            if(count==N):
                X.append(sum)
        print X
        Z.append(len(X))

    else:
        for i in range(10,1-K):
            m=i
            n=N-1
            sum=0
            count=0
            while(n>=0 and m<=9 and m>=0):
                sum=sum+(m*(10**n))
                n=n-1
                m=m+K
                count=count+1
            if(count==N):
                X.append(sum)
        print X
        Z.append(len(X))


for i in range(len(Z)):
    print Z[i]
