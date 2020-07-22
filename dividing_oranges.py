from collections import defaultdict

n,k = map(int, input().split())

mul = n*k

arr = list(map(int, input().split()))
visited = defaultdict(bool)

total = []

for i in range(k):
    visited[arr[i]] = True
    total.append([arr[i]])

x = 0
for i in range(1,mul+1):
    if(len(total[x]) == n):
        x += 1

    if(x == k):
        break

    if not visited[i]:
        total[x].append(i)

for i in range(len(total)):
    print(* total[i])


    
