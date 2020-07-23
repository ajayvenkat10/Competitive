t = int(input())

while(t):
    t-=1
    n,k =  map(int,input().split())
    arr = list(map(int,input().split()))

    for i in range(k):
        arr[i%n] = arr[i%n] ^ arr[n-(i%n)-1]

    print(*arr)
