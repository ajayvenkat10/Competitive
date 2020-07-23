import math as mt
def numOfIncSubseqOfSizeK(arr, n, k):

    dp = [[0 for i in range(n)]
             for i in range(k)]

    for i in range(n):
        dp[0][i] = 1

    for l in range(1, k):
         for i in range(l, n):

            dp[l][i] = 0
            for j in range(l - 1, i):
                if (arr[j] < arr[i]):
                    dp[l][i] += dp[l - 1][j]


    Sum = 0
    for i in range(k - 1, n):
        Sum += dp[k - 1][i]
    return Sum

n,k = map(int, input().split())
arr = list(map(int, input().split()))

length = min(len(set(arr)),k)
count = 1 + len(arr)
if(k > 1):
    for i in range(2,k+1):
        count += numOfIncSubseqOfSizeK(arr, n, i)

print(count % 1000000007)
