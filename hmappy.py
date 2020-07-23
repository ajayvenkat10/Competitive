t = input().split()

N = int(t[0])
M = int(t[1])

linked = []
balloon_list = []
balloons = input().split()
candies = input().split()

for i in range(N):
    balloon_list.append(int(balloons[i]))

sum = sum(balloon_list)
largest = 0
if(sum == M):
    print(0)

else:
    for i in range(N):
        linked.append([int(balloons[i])*int(candies[i]), int(candies[i])])

    # print(max(linked)[0])
    for i in range(M):
        largest = max(linked)
        largest[0] -= largest[1]

    print(max(linked)[0])
