t = int(input())
for i in range(t):
    n = int(input())
    line = input().split()
    cost = []
    best = []
    for i in range(n):
        cost.append(int(line[i]))

    if(n==1):
        print(cost[0])
    else:
        best.extend(cost[:2])
        for i in range(2,len(cost)):
            best.append(cost[i] + min(best[i-1],best[i-2]))

        print(best[-1])
