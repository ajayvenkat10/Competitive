t=int(input())
for i in range(0,t):
    n,k=map(int,input().split())
    u = 0
    if n==2:
        if k==1:
            u=0
        else:
            z=(k-1)*(k)
            u=z//2

    else:
        if k<=n:
            u=k-1

        else:
            d=k-1;
            u=k-1;
            if(d%(n-1))!=0:
                num=(d//(n-1))+1
            else:
                num=(d//(n-1)
            u = (num*(2*d+((num-1)*(-(n-1)))))//2

    print(u%1000000007)
