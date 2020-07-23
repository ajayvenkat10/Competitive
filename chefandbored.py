t = int(input())

for i in range(t):
    n = int(input())
    ans = 0
    while(n>=0):
        ans+= n*n
        n=n-2

    print(ans)
