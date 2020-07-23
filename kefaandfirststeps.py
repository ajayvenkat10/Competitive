# n = int(input())
# arr = list(map(int,input().split()))
#
# dp = [1]*n
#
# for i in range(1,n):
#     if(arr[i] >= arr[i-1]):
#         dp[i] = dp[i-1] + 1
#
# print(max(dp))

from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))

visited = [0]*n
ring_size = defaultdict(int)

visited[0] = 1
visited[arr[0]] = 1
count = 1
if(0 == arr[0]):
    ring_size[1] = 1
else:
    ring_size[1] = 2

for i in range(1,len(arr)):
    if(visited[i] ^ visited[arr[i]]):
        if(visited[i]):
            visited[arr[i]] = visited[i]
        else:
            visited[i] = visited[arr[i]]
        ring_size[visited[i]] += 1

    elif(visited[i] and visited[arr[i]]):
        continue

    else:
        count += 1
        visited[i] = count
        visited[arr[i]] = count
        if(i == arr[i]):
            ring_size[count] += 1
        else:
            ring_size[count] += 2

print(max(list(ring_size.values())))
