t = int(input(""))
for i in range(t):
    num = 0
    denom = 0
    pin = int(input(""))
    num = 1
    if(pin==1):
        denom = 1

    else:
        if(pin%2==0):
            denom = 10**(pin-(int(pin/2)))

        else:
            denom = 10**(pin-(int(pin/2))-1)
