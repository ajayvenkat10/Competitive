t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    odd_count = 0
    ans = True
    for i in range(n):
        if(arr[i] % 2 == 1):
            odd_count += 1

    if(k > odd_count or (k-odd_count) % 2 == 1):
        ans = False

    else:

        ans_arr = []
        i = 0
        while(k > 1):
            if(arr[i] % 2 == 1):
                ans_arr.append(i+1)
                k -= 1

            i += 1

        ans_arr.append(n)

    if(ans):
        print("YES")
        print(*ans_arr)

    else:
        print("NO")
