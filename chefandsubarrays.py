t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        or_result = 0
        for j in range(i,n):
            or_result |= arr[j]

            if(or_result >= k):
                ans += (n - j)
                break

    print(ans)
