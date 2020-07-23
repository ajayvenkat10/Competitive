t=int(raw_input(""))
Z=[]
for i in range(t):
    a=raw_input("")
    a=a.split()
    N=int(a[0])
    K=int(a[1])
    X=[]

    if(K>=0 and K*-1==-K):
        ans=(9-K)*(10**(N-2))

    else:
        ans=(10+K)*(10**(N-2))
    Z.append(ans)

for i in range(len(Z)):
    print Z[i]
