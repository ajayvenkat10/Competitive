t = int(input())

for i in range(t):
    line = input().split()
    n,k = int(line[0]),int(line[1])

    line1 = input().split()
    arr = []
    for i in range(n):
        arr.append(int(line1[i]))

    arr.sort()
    mid = n//2
    if(k>n//2):
        k = n-k

    son = sum(arr[:k])
    father = sum(arr[k:])

    print(father-son)
