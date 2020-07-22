t = int(input())

for i in range(t):
    n,q = map(int, input().split())

    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    prefix_sum = [arr[0]]

    for i in range(1,len(arr)):
        prefix_sum.append(prefix_sum[i-1] + arr[i])

    for i in range(len(queries)):

        low = 0
        high = n-1

        while(low < high):
            mid = (low + high)//2

            if(prefix_sum[mid] >= queries[i]):
                high = mid

            else:
                low = mid + 1

        print(low+1)

    
