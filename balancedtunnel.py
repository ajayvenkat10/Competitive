from collections import defaultdict

n = int(input())

enter = list(map(int, input().split()))
exit = list(map(int, input().split()))

enter = enter[::-1]
exit = exit[::-1]

next_enter = defaultdict(set)
next_exit = defaultdict(set)

count = 0
for i in range(n):
    next_enter[enter[i]] = set(enter[:i])
    next_exit[exit[i]] = set(exit[:i])

for i in range(len(enter)):
    x = next_enter[enter[i]]
    y = next_exit[enter[i]]

    if(len(x) == 0):
        if(len(y) != 0):
            count += 1

    else:
        if(len(y)!=0):
            if(len(x.union(y)) > len(x)):
                count += 1


print(count)
