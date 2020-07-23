t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        line = input()
        arr.append(line)

    ans = arr[0]

    for i in range(1,n):
        ans = set(ans) & set(arr[i])

    print(len(list(set(ans))))
