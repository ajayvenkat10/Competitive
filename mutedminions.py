t = int(input())

for i in range(t):
    line = input().split()
    n,k = int(line[0]),int(line[1])

    arr = input().split()
    count = 0
    for i in range(n):
        if((int(arr[i]) + k)%7 == 0):
            count+=1

    print(count)
