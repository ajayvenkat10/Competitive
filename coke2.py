t = int(input())
for i in range(t):
    n,m,k,l,r = map(int, input().split())
    C = []
    P = []
    for i in range(n):
        c,p = map(int, input().split())
        C.append(c)
        P.append(p)

    ans = []
    for i in range(n):
        if(C[i]< k):
            mid = min(C[i] + m , k)
        elif(C[i] > k):
            mid = max(C[i] - m , k)
        else:
            mid = k

        if(mid<=r and mid>=l):
            ans.append(P[i])

    if(ans == []):
        print(-1)
    else:
        print(min(ans))
