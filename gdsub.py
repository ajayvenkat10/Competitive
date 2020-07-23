from collections import defaultdict

n,k = map(int, input().split())
arr = list(map(int, input().split()))
count = defaultdict(int)

for i in range(len(arr)):
    count[arr[i]] += 1

distinct = list(count.keys())
distinct_values = list(count.values())

prefix_sum = [0]*len(distinct)
prefix_sum[-1] = distinct_values[-1]

for i in range(len(distinct_values)-2,-1,-1):
    prefix_sum[i] = distinct_values[i] + prefix_sum[i+1]

prefix_sum.append(0)

ans = 0
final = 0
ans = len(arr)+1
if(k>1):
    for i in range(2,k+1):
        for j in range(len(distinct)-(i-1)):
            final = distinct_values[j]
            for k in range(j+1,i):
                final *= (prefix_sum[k] - prefix_sum[len(prefix_sum)-i + 1])

            ans += final

print(ans % 1000000007)
