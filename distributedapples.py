t = int(input())

for i in range(t):
    N,K = map(int, input().split())

    if((N//K) % K == 0):
        print("NO")

    else:
        print("YES")
