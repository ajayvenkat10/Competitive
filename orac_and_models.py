import math

def findAllFactors(n):
    factors = [1]

    for i in range(2, int(math.sqrt(n))+1):
        if(n % i == 0):
            factors.append(i)
            factors.append(n//i)

    return factors


t = int(input())

for i in range(t):
    n = int(input())
    sizes = list(map(int, input().split()))
    sizes.insert(0, 0)

    dp = [1] * len(sizes)
    ans = 1

    for i in range(2, n+1):
        facts = findAllFactors(i)
        count = 1

        for j in range(len(facts)):
            if(sizes[facts[j]] < sizes[i]):
                count = max(count, dp[facts[j]] + 1)

        dp[i] = count
        ans = max(ans, count)

    print(ans)

