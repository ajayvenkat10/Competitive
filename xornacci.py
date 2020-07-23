t = int(input())

for i in range(t):
    a,b,n = map(int, input().split())

    arr = [a,b]

    arr.append(a^b)

    print(arr[n%3])
    
    