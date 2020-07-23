from fractions import gcd
n=int(raw_input(""))
R=[]
Z=[]
C=0
for i in range(n):
    Z=[]
    C=0
    a=raw_input("")
    a=a.split()
    for i in range(2):
         Z.append(int(a[i]))

    A=Z[0]
    B=Z[1]

    if(A==0 or B==0 or A==B):
        R.append(A+B)
    elif(B<A):
        if(A%B==0):
            R.append(2*B)
        else:
            x=gcd(A,B)
            R.append(2*x)
    else:
        if(B%A==0):
            R.append(2*A)
        else:
            x=gcd(A,B)
            R.append(2* x)

for i in range(len(R)):
    print R[i]
