from fractions import Fraction
t = int(input(""))

for i in range(t):
    num = 0
    denom = 0
    pin = int(input(""))

    if(pin==1):
        num = 1
        denom =1

    else:
        num = 1
        denom = 10**(int(pin/2))
        # else:
            # denom = 10**(pin-int(pin/2)-1)

    print(("%d %d") % (num,denom))
