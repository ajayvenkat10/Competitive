from collections import defaultdict

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = defaultdict(bool)

    odd = []
    even = []

    for i in range(n):
        if(arr[i] % 2 == 1):
            odd.append(arr[i])
        else:
            even.append(arr[i])

        freq[arr[i]] = True

    flag = False
    if(len(odd) % 2 == 0 and len(even) % 2 == 0):
        flag = True

    else:
        for i in range(len(odd)):
            if(freq[odd[i]+1] or freq[odd[i]-1]):
                flag = True
                break

    if(flag):
        print("YES")

    else:
        print("NO")
