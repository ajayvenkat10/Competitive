from collections import defaultdict

t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))

    dict = defaultdict(list)

    for i in range(len(arr)):
        dict[i//n].append(arr[i])

    keys = list(dict.keys())
    flag = 1
    for i in range(len(keys)):
        x = dict[keys[i]]

        if(len(x) != len(set(x))):
            flag = 0
            break

    if(flag):
        print("YES")

    else:
        print("NO")
