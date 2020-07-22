t = int(input())

for i in range(t):
    n,k = map(int, input().split())

    x = k // (n-1)
    y = k % (n-1)

    if(y != 0):
        ans = (n * x) + (y)

    else:
        ans = (n * x) + (y-1)
        
    print(ans)