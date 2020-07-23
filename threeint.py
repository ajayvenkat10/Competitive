n=int(raw_input(""))
X=[]
Y=[]
count=0
for i in range(n):
    X=[]
    count=0
    a= raw_input("")
    a=a.split()
    for i in range(3):
        b=int(a[i])
        X.append(b)

    A=X[0]
    B=X[1]
    C=X[2]

    if(2*B==C+A):
        count=0
    else:
        Z=C+A
        if(Z%2==0):
            x=Z/2
            num=B-Z/2
            count=abs(num)

        else:
            if(A>0):
                A=A-1
            else:
                A=A+1
            Z=C+A
            x=Z/2
            num=B-x
            count=abs(num)
    Y.append(count)

for i in range(len(Y)):
     print Y[i]
