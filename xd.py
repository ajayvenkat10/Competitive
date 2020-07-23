A=[]

n=int(raw_input(""))

for i in range(n):
    Z=""
    a=int(raw_input(""))
    while(a!=0):
        if(a<3):
            a=a-1
            Z=Z+"D"

        else:
            a=a-3
            Z=Z+"XD"

    A.append(Z)

for i in range(len(A)):
    print A[i]
