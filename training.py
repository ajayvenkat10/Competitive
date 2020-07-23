t = int(input())
case_count = 0
for i in range(t):
    case_count += 1
    line = input().split()
    n,p = int(line[0]),int(line[1])
    line1 = input().split()
    arr = []
    count_arr = [0] * 10005
    for i in range(n):
        arr.append(int(line1[i]))
        count_arr[int(line1[i])] += 1

    elements_set = list(set(arr))
    elements_set.sort(reverse = True)

    final = []

    for i in range(len(elements_set)):
        count = count_arr[elements_set[i]]
        rem = p
        if(count <= rem):
            f = count
        else:
            f = rem
        rem = rem - f
        sum = 0
        j = i+1
        while(rem > 0 and j<len(elements_set)):
            if(rem >= count_arr[elements_set[j]]):
                x = count_arr[elements_set[j]]
            else:
                x = rem
            rem = rem - x
            sum+= elements_set[i]*x - elements_set[j]*x
            j+=1

        if(rem==0):
            final.append(sum)

    print("Case #%d: %d" % (case_count,min(final)))
