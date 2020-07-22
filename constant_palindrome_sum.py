from collections import defaultdict

t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    max_arr = []
    min_arr = []

    part1 = arr[:n//2]
    part2 = arr[n//2:]
    part2 = part2[::-1]

    sum_count = defaultdict(int)

    for i in range(n//2):
        greater = max(part1[i], part2[i])
        smaller = min(part1[i], part2[i])
        max_arr.append(greater)
        min_arr.append(smaller)

        sum_count[part1[i] + part2[i]] += 1

    sums = list(sum_count.keys())

    min_arr.sort()
    max_arr.sort()

    ans = n//2

    for ind_sum in sums:

        low = 0
        high = n//2 - 1

        if(ind_sum > k):
            while(low < high):
                mid = (low + high)//2
                if(ind_sum - max_arr[mid] <= k):
                    high = mid
                else:
                    low = mid + 1

            ans1 = (n//2 - low) - sum_count[ind_sum] + (low * 2)

        else:
            while(low < high):
                mid = (low + high)//2
                if(min_arr[mid] < ind_sum):
                    low = mid + 1
                else:
                    high = mid

            if(min_arr[low] < ind_sum):
                low += 1

            ans1 = low - sum_count[ind_sum] + ((n//2 - low) * 2)

        ans = min(ans, ans1)

    print(ans)
