t = int(input())

for i in range(t):
    N = int(input())
    arr = []
    line1 = input().split()

    for i in range(N):
        arr.append(int(line1[i]))

    min_val = min(arr)
    indices = [i for i, x in enumerate(arr) if x == min_val]
    if(len(indices)>1):
        pos = indices[1]
    else:
        pos = indices[0]
    print(pos)

    # if(pos == 0):
    #     if(all(arr[i] <= arr[i+1] for i in range(1,len(arr)-1))):
    #         print("YES")
    #
    #     else:
    #         print("NO")


    part1 = arr[:pos]
    part2 = arr[pos:]

    if(all(part1[i] <= part1[i+1] for i in range(len(part1)-1))):
        if(all(part2[i] <= part2[i+1] for i in range(len(part2)-1))):
            print("YES")

        else:
            print("NO")
    else:
        print("NO")
