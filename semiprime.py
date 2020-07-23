import math

def checkSemiprime(num):
    cnt = 0

    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break
    if(num > 1):
        cnt += 1

    return cnt == 2

def semiprime(n):
    if checkSemiprime(n) == True:
        return True
    else:
        return False

def isPerfectSquare(x):

    sr = math.sqrt(x)
    return ((sr - math.floor(sr)) == 0)

t = int(input())

for i in range(t):
    N = int(input())
    ans = False

    for i in range(2,(N//2)+1):
        if( isPerfectSquare(i) == False):
            if(semiprime(i)):
                if(isPerfectSquare(N-i) == False):
                    if(semiprime(N-i)):
                        ans = True
                        break

    if(ans):
        print("YES")

    else:
        print("NO")
