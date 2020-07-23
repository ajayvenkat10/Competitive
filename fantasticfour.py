n = int(input())
arr = []
invalid = []
line = input().split()
count_arr = [0] *4
count = 0

for i in range(n):
    arr.append(int(line[i]))

for i in range(len(arr)):
    if(arr[i]%4 != 0):
        invalid.append(arr[i]%4)

if(sum(invalid) %4 != 0):
    print(-1)

else:
    for i in range(len(invalid)):
        count_arr[invalid[i]] += 1

    count+= count_arr[2]//2

    count_arr[2] = count_arr[2]%2

    min_count = min(count_arr[1],count_arr[3])
    count+= min_count

    count_arr[1] -= min_count
    count_arr[3] -= min_count

    if(max(count_arr) == 0):
        print(count)

    elif(max(count_arr) == 1):
        print(-1)

    else:
        if(count_arr[1]>0):
            count_arr[0] = count_arr[1]
        else:
            count_arr[0] = count_arr[3]

        if(count_arr[2] == 0):
            if(count_arr[0]%4 == 0):
                count+= count_arr[0] - count_arr[0]//4
                ans = count
            else:
                ans = -1

        else:
            if(count_arr[0]%2 != 0):
                ans = -1

            else:
                if((count_arr[0]//2)%2 == 1):
                    count+= count_arr[0] - count_arr[0]//4 + 2
                    ans = count
        # print(count_arr)
        print(ans)
