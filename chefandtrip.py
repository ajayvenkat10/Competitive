import random
t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    arr = list(map(int, input().split()))

    flag = 0

    total = list(range(1,k+1))

    for i in range(n):
        if(arr[i] == -1):
            if(i !=0 and i!=n-1):
                if(arr[i+1] != -1):
                    if(len(total) == 2 and arr[i-1] != arr[i+1]):
                        flag = 1
                        break

                    for j in range(len(total)):
                        if(total[j]!=arr[i-1] and total[j]!=arr[i+1]):
                            arr[i] = total[j]
                            break
                else:
                    for j in range(len(total)):
                        if(total[j]!=arr[i-1]):
                            arr[i] = total[j]
                            break

            else:
                if(i == 0):
                    if(arr[i+1] == -1):
                        arr[i] = total[0]

                    else:
                        for j in range(len(total)):
                            if(total[j]!=arr[j-1]):
                                arr[i] = total[j]
                                break
                else:
                    for j in range(len(total)):
                        if(total[j]!=arr[i-1]):
                            arr[i] = total[j]
                            break

            if(arr[i] == -1):
                flag = 1
                break

    if(flag):
        print("NO")

    else:
        print("YES")
        print(*arr)
