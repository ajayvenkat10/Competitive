t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    if(n == 1 or n==2):
        ans = 0 

    else:
        pos = 0
        mini = arr[-1]
        for i in range(n-2, -1 , -1):
            mini = min(arr[i], mini)

            if(mini == arr[i] or mini == arr[-1]):
                pos = pos  
            else:
                pos = i+1
                break 
            
            # if(i > 0):
            #     if(arr[i+1] > arr[i] and arr[i-1] > arr[i]):
            #         pos = i
            #         break 

        ans = pos

    print(ans)