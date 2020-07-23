t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    valid = 1

    for i in range(1,n):
        start = max(0,i-5)
        if(min(prices[start:i]) > prices[i]):
            valid += 1

    print(valid)
