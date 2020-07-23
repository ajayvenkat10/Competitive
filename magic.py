import sys
n=int(raw_input(""))
A=[]
Z=[]
sum=0
count=0
for i in range(n):
    A=[]
    count=0
    a=raw_input("")
    a=a.split()
    N=int(a[0])
    K=int(a[1])

    b=raw_input("")
    b=b.split()
    for i in range(N):
        A.append(int(b[i]))

    # print A
    if(N==1):
        print 0
        sys.exit()

    for i in range(N):
        C=[]
        x=i
        for i in range(N):
            if (i!=x):
                C.append(A[i])
        # print C
        Y=A[x]+K
        # print Y
        sum=0
        for i in range(len(C)):
            sum=sum+C[i]
        # print sum
        if(Y>sum):
            count=count+1
        # print count
    Z.append(count)

for i in range(len(Z)):
    print Z[i]
