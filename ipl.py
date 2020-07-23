N = int(input())
cost = []
line = input().split()

for i in range(N):
    cost.append(int(line[i]))

if(N==1):
    print(cost[0])

if(N==2):
    print(cost[0]+cost[1])

best_cost = [0]*N
best_cost[0] = cost[0]
best_cost[1] = cost[1] + best_cost[0]
best_cost[2] = max( best_cost[1], cost[2]+max(cost[1],cost[0]))

for i in range(3,N):
    best_cost[i] = max(best_cost[i-1], cost[i]+best_cost[i-2], cost[i]+cost[i-1]+best_cost[i-3])

print(best_cost[-1])
