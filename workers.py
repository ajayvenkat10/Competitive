n=int(raw_input(""))
C=[]
T=[]

X=[]
Y=[]
Z=[]
c=raw_input("")
c=c.split()
for i in range(n):
    C.append(int(c[i]))

t=raw_input("")
t=t.split()
for i in range(n):
    T.append(int(t[i]))

for i in range(n):
    if(T[i]==1):
        X.append(C[i])
    elif(T[i]==2):
        Y.append(C[i])
    else:
        Z.append(C[i])

if(len(X)==0 or len(Y)==0):
    Z.sort()
    print Z[0]

elif(len(Z)==0):
    X.sort()
    Y.sort()
    print X[0]+Y[0]

else:
    X.sort()
    Y.sort()
    Z.sort()

    R=X[0]+Y[0]
    if(R>Z[0]):
        print Z[0]
    else:
        print R
