import math

t = int(input())

while(t):
    n,k = map(int, input().split())
    ans = 0

    if(k<n-1 or (k > (n * (n+1))//2)):
        ans = -1

    else:
        if(k>= n-1 and k<= n+1):
            if(n==1 or n==2):
                if(n==1):
                    if(k<=n):
                        ans = k

                else:
                    if(k==1):
                        ans = k
                    else:
                        ans = 2
            else:
                ans = 2


        elif(k>n+1 and k<= n*2):
            ans = 3

        else:
            x = math.ceil(k/n)
            if(k%n <= n//2 and k%n != 0):
                ans = 2*x - 2

            else:
                ans = 2*x -1

    print(ans)
    t -= 1

 # if(n%2 == 1):
 #     if(k % n >= math.ceil(n/2) or  k%n == 0):
 #         ans = math.ceil(k/n) + (math.ceil(k/n)-1)
 #
 #     else:
 #         ans = math.ceil(k/n) + (math.ceil(k/n)-2)
 #
 # else:
 #     if(k % n > math.ceil(n/2) or  k%n == 0):
 #         ans = math.ceil(k/n) + (math.ceil(k/n)-1)
 #
 #     else:
 #         ans = math.ceil(k/n) + (math.ceil(k/n)-2)
