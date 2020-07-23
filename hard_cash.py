t =  int(input())

for i in range(t):
    n,k = map(int, input().split())
    coins = list(map(int, input().split()))

    print(sum(coins) % k)
