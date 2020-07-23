t = int(input())

for i in range(t):
    n = int(input())

    count = 0
    flag = 0

    while(True):
        n -= 9
        count += 1
        if(n<0):
            flag = 1
            break

        if(n%10 == 0):
            break

    if(flag):
        print(-1)

    else:
        print(count)
