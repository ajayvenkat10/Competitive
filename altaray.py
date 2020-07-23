t = int(input())

for i in range(t):
    n = int(input())
    line = input().split()
    arr = []

    for i in range(n):
        arr.append(int(line[i]))

    dp = [1]*n

    for i in range(n-2,-1,-1):
        if(arr[i] * arr[i+1] < 0):
            dp[i] = dp[i+1]+1

    print(*dp)
