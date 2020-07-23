def min_hits(n, hits_arr, z):
    sum_array = [0]
    for i in range(1,n+1):
        sum_array.append(hits_arr[i-1]+sum_array[i-1])

    count = 0
    ans = 1000000000000

    for i in range(n-1, z-2, -1):
        hits = count*hits_arr[i] + sum_array[i+1] - sum_array[i-z+1]
        print(hits)
        ans = min(hits, ans)
        count+=1
    print("hey")
    if(z==1):
        return ans

    else:
        for i in range(1,n):
    	       hits_arr[i] -= hits_arr[0]

        return min(ans, hits_arr[0]*n + min_hits(n-1, hits_arr[1:], z-1))



t = int(input())
for i in range(t):
    n, z = map(int, input().split())
    hits_array = list(map(int, input().split()))
    hits_array.sort()
    print(min_hits(n, hits_array, z))
