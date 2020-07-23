from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
ans = n-1

for i in range(n):
    frequency = defaultdict(int)
    valid_prefix = True
    for j in range(i):
        frequency[arr[j]] += 1
        if(frequency[arr[j]] == 2):
            valid_prefix = False
            break

    suffix = n
    j = n-1
    while(j>=i):
        frequency[arr[j]] += 1
        if(frequency[arr[j]] == 1):
            suffix = j
        else:
            break
        j -= 1

    if(valid_prefix):
        ans = min(ans,suffix-i)

print(ans)
