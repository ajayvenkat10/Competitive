t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    odd = 0
    even = 0

    false_odd = 0
    false_even = 0

    for i in range(n):
        if(arr[i]%2 == 0):
            even += 1
        else:
            odd += 1 

        if(arr[i]%2 == 0 and i%2 != 0):
            false_even += 1
        
        if(arr[i]%2 == 1 and i%2 != 1):
            false_odd += 1


    if(odd != n//2):
        ans = -1

    else:
        if(false_even == false_odd):
            ans = false_odd

        else:
            ans = -1

    print(ans)