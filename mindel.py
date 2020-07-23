from fractions import gcd

def gcd_n(numbers):
    return reduce(lambda x, y: gcd(x, y), numbers)

n=int(raw_input(""))
Z=[]
for i in range(n):
    X=[]
    a=int(raw_input(""))
    b=raw_input("")
    b=b.split()
    for i in range(a):
        X.append(int(b[i]))

    X.sort()

    if(gcd_n(X)==1):
        Z.append(0)

    else:
        Z.append(-1)

for i in range(len(Z)):
    print Z[i]
