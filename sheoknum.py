import math

def isPower (num, base):
    if base == 1 and num != 1: return False
    if base == 1 and num == 1: return True
    if base == 0 and num != 1: return False
    power = int (math.log (num, base) + 0.5)
    return base ** power == num

t = int(input(""))

for i in range(t):
    N = int(input(""))

    if(isPower(N,2)):
        if(N==1):
            print(2)
        else:
            print(1)

    else:
        x = 0
        num = 2**x
        while(N>num):
            x+=1
            num = 2**x
        x1=x
        x = x-1
        num = 2**x

        M = N-num

        if(isPower(M,2)):
            print(0)

        else:
            y1 = 0
            num1 = 2**y1

            while(M>num1):
                y1 += 1
                num1 = 2**y1

            y2 = y1-1
            num2 = 2**y2

            ans1 = num1-M
            ans2 = M-num2

            if(y2==x):
                ans2 = (2**x1-N)+1

            if(y1==x):
                ans1 = (2**x1-N)+1

            print(min(ans1,ans2))
