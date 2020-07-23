t = int(input())

for i in range(t):
    line = input().split()
    n,k = int(line[0]), int(line[1])
    ans = 0
    initial = k-1
    if(n>=k):
        ans = initial

    else:
        ans = initial
        end = k+n-1
        balance = k*2 - end -1
        if(n==2):

            ans += (balance * (balance+1))//2

        else:
            interval = initial - balance
            while(True):
                ans += balance
                balance-= interval
                if(balance <= 0):
                    break

    print(ans%(1000000007))
