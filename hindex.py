t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    final = [1]

    val = 2
    for i in range(1,len(arr)):
        count = 0
        for j in range(i+1):
            if(arr[j] >= val):
                count += 1

        if(count>=val):
            final.append(val)
            val += 1

        else:
            final.append(val-1)

    print("Case #%d: " % (_+1) , end="")
    print(*final)
