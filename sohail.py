from collections import defaultdict

n,m = map(int,input().split())
arr = list(map(int,input().split()))

distinct = defaultdict(int)
dp = [0]*n
dp[-1] = 1
distinct[arr[-1]] = 1

for i in range(n-2,-1,-1):
    if(distinct[arr[i]] == 0):
        distinct[arr[i]] = 1
        dp[i] = dp[i+1] + 1

    else:
        dp[i] = dp[i+1]

for i in range(m):
    a = int(input())

    print(dp[a-1])
