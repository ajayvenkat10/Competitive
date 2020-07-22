t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    ans = -1
    for i in range(1, 1025):

        x = set()
        for j in range(n):
            x.add(arr[j] ^ i)

        if(x == set(arr)):
            flag = True 
            ans = i 
            break 

    print(ans)