t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    final = [0] * n
    final[-1] = arr[-1] 
    minimum = final[-1]
    count = 0
    for i in range(n-2,-1,-1):
        minimum = min(minimum, arr[i])
        final[i] = minimum
    
        if(arr[i] > final[i]):
            count += 1

    print(count)

