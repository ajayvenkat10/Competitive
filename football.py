t = int(input())

for i in range(t):
    n = int(input())
    goals = list(map(int, input().split()))
    fouls = list(map(int, input().split()))

    maximum = 0
    for i in range(n):
        maximum = max(0,maximum, 20*goals[i] - 10*fouls[i])

    print(maximum)
