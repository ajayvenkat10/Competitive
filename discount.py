t = int(input())

for i in range(t):
    n = int(input())
    n = str(n)
    arr = list(n)

    maxi = '-1'
    pos = 0

    start = arr[0]

    for i in range(1,len(arr)):
        if(arr[i] >= start):
            if(arr[i] > start):
                start = arr[i]
                pos = i

        else:
            break

    del(arr[pos])

    arr = ''.join(arr)
    arr = int(arr)

    print(arr)
