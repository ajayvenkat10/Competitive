n=int(raw_input(""))
R=[]
Z=[]
C=0
for i in range(n):
    Z=[]
    C=0
    a=raw_input("")
    a=a.split()
    # for i in range(2):
        # Z.append(int(a[i]))

    A=int(a[0])
    B=int(b[0])

    while(A!=B):
        if(A==0 or B==0):
            break

        elif(A<B):
            B=B-A

        else:
            A=A-B

    C=A+B
    R.append(C)

for i in range(len(R)):
    print R[i]
