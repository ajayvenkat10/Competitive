t = int(input())

arr = list(map(int, input().split()))

x = set()

for num in arr:
    if(num <= t):
        x.add(num)

print(t - len(x))