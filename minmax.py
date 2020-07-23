t = int(input())

for i in range(t):
    n = int(input())
    k = int(input())

    ans = 0

    if(k%n <= n//2):
        ans = (k%n) * 2
        if(k%n == n//2):
            if(n%2 == 0):
                ans = (((k%n)-1) * 2) + 1
    else:
        if(n%2 == 0):
            ans = ((k%n) - 2 * ((k%n) - (n//2))) * 2
        else:
            ans = ((k%n) - (2 * ((k%n) - (n//2))) +1) * 2

    print(ans)
