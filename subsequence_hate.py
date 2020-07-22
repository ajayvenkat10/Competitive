t = int(input())

for i in range(t):

    binary = input()

    dp = []
    for i in range(4):
        dp.append([0]*(len(binary)+1))

    current = binary[0]

    i = 0
    continuous_count = 0
    j = 1

    while(i< len(binary)):
        while(i < len(binary) and binary[i]==current):
            i+=1
            continuous_count+=1

        if(current == '0'):
            dp[0][j] = dp[0][j - 1]
            dp[1][j] = dp[1][j - 1] + continuous_count
            dp[2][j] = dp[2][j - 1] + continuous_count
            dp[3][j] = min(dp[3][j - 1], dp[1][j - 1])

        else:
            dp[0][j] = dp[0][j - 1] + continuous_count
            dp[1][j] = dp[1][j - 1]
            dp[2][j] = min(dp[2][j - 1], dp[0][j - 1])
            dp[3][j] = dp[3][j - 1] + continuous_count

        if(i>=len(binary)):
            break

        j+=1
        current = binary[i]
        continuous_count = 0
    
    print(min(dp[0][j],dp[1][j],dp[2][j],dp[3][j]))

