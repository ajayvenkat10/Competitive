n,k= map(int, input().split())

arr = list(map(int, input().split()))

count = 0

for i in range(n):
    if(arr[i] + k <= 5):
        count += 1

print(count//3)
