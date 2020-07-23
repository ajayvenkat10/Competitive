n = int(input())
cost = list(map(int, input().split()))

dp = [0]*n
dp[1] = abs(cost[0] - cost[1])

for i in range(2,n):
    dp[i] = min(dp[i-2] + abs(cost[i] - cost[i-2]), dp[i-1] + abs(cost[i] - cost[i-1]))

print(dp[n-1])
