t = int(input())

for i in range(t):

    n,k = map(int, input().split())

    ans = ((k+1) * pow(2,n,1000000007)) % 1000000007

    ans =  ans - (k+1) * 2 + 1

    print(ans)