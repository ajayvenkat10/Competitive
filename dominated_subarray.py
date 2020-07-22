from collections import defaultdict

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    frequency =  defaultdict(int)

    if(n == 1 or len(set(arr)) == n):
        ans = -1

    else:
        start = 0
        best_ans = n

        for i in range(n):
            frequency[arr[i]] += 1
            if(frequency[arr[i]] > 1):
                while(frequency[arr[start]] == 1):
                    frequency[arr[start]] -= 1
                    start += 1

                best_ans = min(best_ans, i-start+1)
                frequency[arr[start]] -= 1
                start += 1

        ans = best_ans

    print(ans)