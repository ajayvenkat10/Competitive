from fractions import Fraction
t = int(input(""))

for i in range(t):
    num = 0
    denom = 0
    pin = int(input(""))

    limit = 10**pin
    count = 0
    if(pin == 1):
        start = 0
    else:
        start = 10**(pin-1)

    for i in range(start,limit):
        if(str(i) == str(i)[::-1]):
            count+=1

    ans = Fraction(count,limit-start)
    num = ans.numerator
    denom = ans.denominator

    print(("%d %d") % (num,denom))
