t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    sum_less = 0
    pos = -1
    for i in range(len(arr)):
        if(arr[i] <= k):
            sum_less += arr[i]

        else:
            pos = i
            break

    if(pos == len(arr)-1 or pos == -1):
        ans = sum(arr)

    else:
        m = n-pos

        prefix_sum = 0
        for i in range(pos,len(arr)):
            arr[i] -= k
            prefix_sum += arr[i]

        prefix_sum = prefix_sum - arr[-1] - arr[-2]

        if(prefix_sum < arr[-2]):
            ans = sum_less + m*k + arr[-1] - arr[-2] + prefix_sum

        else:
            ans = sum_less + m*k + arr[-1]
            if((prefix_sum + arr[-2]) %2 == 1):
                ans -= 1

    print(ans)
