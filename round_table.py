t = int(input())
for i in range(t):
    n = int(input())
    line = input().split()
    cost = []
    best = []
    best1 = []

    for i in range(n):
        cost.append(int(line[i]))

    cost1 = cost[::-1]

    if(n==1):
        print(cost[0])

    else:
        best.extend(cost[:2])
        for i in range(2,len(cost)):
            best.append(cost[i] + min(best[i-1],best[i-2]))

        best1.extend(cost1[:2])
        for i in range(2,len(cost1)):
            best1.append(cost1[i] + min(best1[i-1],best1[i-2]))

        print(min(best[-1],best1[-1]))
