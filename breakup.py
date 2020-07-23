n = int(input())
arr = list(map(int, input().split()))

dp = [n]*n

for i in range(n):
    for j in range(i+1):
        sub_arr = arr[j:i+1]

        if(sub_arr == sub_arr[::-1]):
            if(j==0):
                dp[i]=1

            else:
                dp[i] = min(dp[i],dp[j-1]+1)

print(dp[-1])
