from collections import defaultdict
t = int(input())

for i in range(t):
    n =  int(input())
    d = defaultdict(int)
    line = input().split()
    arr = []
    for i in range(n):
        arr.append(int(line[i]))

    x = abs(arr[0] - arr[1])
    d[x] += 1
    for i in range(2,n):
        x = abs(arr[0]-arr[i])/i
        d[x] += 1

    keys = list(d.keys())
    diff = 0
    if(len(keys)>2):
        diff = arr[2]-arr[1]

    else:
        max = 0
        for i in range(len(keys)):
            if(d[keys[i]]>max):
                max = d[keys[i]]
                diff = int(keys[i])

    ans = []
    for i in range(1,len(arr)-1):
        x = abs(arr[i] - arr[i-1])
        y = abs(arr[i] - arr[i+1])

        if(x!=diff and y!=diff):
            ans.append(i)

    if(ans==[]):
        x = abs(arr[0]-arr[1])
        y = abs(arr[-1]-arr[-2])

        if(x!=diff):
            ans.append(0)

        elif(y!=diff):
            ans.append(-1)

    if(ans==[]):
        print(*arr)
    else:
        pos = ans[0]

        if(pos == 0):
            arr[pos] = arr[pos+1]-diff

        else:
            arr[pos] = arr[pos-1]+diff

        print(*arr)
