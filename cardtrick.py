t = int(input())

for i in range(t):
    N = int(input())
    arr = []
    line1 = input().split()

    for i in range(N):
        arr.append(int(line1[i]))

    num = arr[0]
    pos = 0

    for i in range(1,len(arr)):
        if(arr[i] >= num):
            num = arr[i]

        else:
            num = arr[i]
            pos = i
            break

    if(pos==0):
        print("YES")
        
    else:

        part1 = arr[:pos]
        part2 = arr[pos:]
        sorted = True
        for i in range(1,len(part2)):
            if(part2[i]<part2[i-1]):
                sorted = False
                break

        if(sorted):
            if(arr[-1]<=arr[0]):
                print("YES")

            else:
                print("NO")

        else:
            print("NO")
