t = input().split()
N = int(t[0])
M = int(t[1])

candies_list = []
balloon_list = []
balloons = input().split()
candies = input().split()
low = 0
mid = 0
max_val = 0

for i in range(N):
    balloon_list.append(int(balloons[i]))

for i in range(N):
    candies_list.append(int(candies[i]))

for i in range(N):
    cost = balloon_list[i]*candies_list[i]
    if(cost > max_val):
        max_val = cost

high = max_val

while(low<high):
    mid = (low+high)//2
    bal_count = 0
    for i in range(N):
        bal_count += max(0,(balloon_list[i] - (mid//candies_list[i])))

    if(bal_count <= M):
        high = mid

    else:
        low = mid+1

print(low)
