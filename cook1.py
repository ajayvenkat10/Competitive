t = int(input())

for i in range(t):
    line = input().split()
    N = int(line[0])
    K = int(line[1])
    arr = []
    line1 = input().split()

    for i in range(N):
        arr.append(int(line1[i]))

    next = 0
    start = 0
    count = 0
    i = 0
    for i in range(N):
        next = arr[i]
        if((next-start) > K):
            if((next-start)%K == 0):
                count += ((next-start)//K)-1
            else:
                count += ((next-start)//K)
        start = next

    print(count)
