t = int(input())

for i in range(t):
    a,b,n = map(int, input().split())

    x = [min(a,b), max(a,b)]

    count = 0

    i = 1
    while(True):
        val = x[i] + x[i-1]
        count += 1

        if(val > n):
            break 

        x.append(val)
        i+=1 

    print(count)

    