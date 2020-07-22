t = int(input())

for i in range(t):
    n = int(input())

    ans = 0

    for i in range(n//2 + 1):
        ans += (8* pow(i,2))

    print(ans) 

    