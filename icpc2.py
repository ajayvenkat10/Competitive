
t = int(input())

for i in range(t):
    line = input().split()
    n,k = int(line[0]), int(line[1])
    arr = []
    final = []
    pos = 0
    flag = False
    arr_list = input().split()
    for i in range(n):
        arr.append(int(arr_list[i]))

    arr.sort()
    i = 0

    if(n == 1):
        print(sum(arr))
    else:
        for i in range(len(arr)):
            if(arr[i] > k):
                pos = i
                flag = True
                break

        if(pos == 0 and flag==False):
            print(sum(arr))

        else:
            final += arr[:pos]
            arr = arr[pos:]
            i = 0
            while(len(arr) >1):
                if(arr[i] <= k):
                    final.append(arr[i])
                    arr = arr[1:]

                if(len(arr) == 1):
                    break

                diff = arr[i]-k
                arr[i] -= diff
                arr[i+1] -= diff

            final+= arr

            print(sum(final))
