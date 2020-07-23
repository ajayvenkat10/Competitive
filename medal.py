t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    a = [arr.index(max(arr)), arr.index(min(arr))]

    a.sort()

    final = []
    for i in range(len(a)):
        final.append(arr[a[i]])

    print(*final)
