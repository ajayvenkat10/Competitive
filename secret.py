n=int(raw_input(""))
Z=[]
for i in range(n):
    a=raw_input("")
    a=a.split()
    X1=float(a[0])
    X2=float(a[1])
    X3=float(a[2])
    V1=float(a[3])
    V2=float(a[4])

    d1=X3-X1
    d2=X2-X3

    p=d1/V1
    q=d2/V2

    if(p==q):
        Z.append("Draw")

    elif(p>q):
        Z.append("Kefa")

    else:
        Z.append("Chef")


for i in range(len(Z)):
    print Z[i]
