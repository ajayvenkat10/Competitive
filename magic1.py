import sys
n=int(raw_input(""))
A=[]
Z=[]
sum=0
count=0
for i in range(n):
    A=[]
    sum=0
    count=0
    a=raw_input("")
    a=a.split()
    N=int(a[0])
    K=int(a[1])

    b=raw_input("")
    b=b.split()
    for i in range(N):
        A.append(int(b[i]))

    for i in range(N):
        sum=sum+int(b[i])

    if(N==1):
        print 0
        sys.exit()

    for i in range(N):
        x=A[i]+K
        y=sum-A[i]
        if(x>y):
            count=count+1
    Z.append(count)

for i in range(len(Z)):
    print(Z[i])
