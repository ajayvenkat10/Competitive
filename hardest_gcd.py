from fractions import gcd

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))

def gcd_n(numbers):
    return reduce(lambda x, y: gcd(x, y), numbers)

t=int(raw_input(""))
A=[]
B=[]
Z=[]
for i in range(t):
    n=raw_input("")
    n=n.split()

    N=int(n[0])
    K=int(n[1])
    A=[]
    a=raw_input("")
    a=a.split()
    for i in range(N):
        A.append(int(a[i]))

    if(gcd_n(A)==1):
        Z.append("YES")

    else:
        if(gcd_n(A)<K):
            Z.append("YES")
        else:
            for i in range(len(A)):
                B.append(factors(A[i]))

            Ans=set.intersection(*B)
            Ans=list(Ans)

            low=0
            high=len(Ans)-1
            while(low<=high):
                mid=(low+high)/2

                if(Ans[mid]>K):
                    if(Ans[mid-1]<K):
                        key=ans[mid-1]
                        break
                    else:
                        high=mid-1
                elif(Ans[mid]<K):
                    if(Ans[mid+1]>K):
                        key=ans[mid]
                        break
                    else:
                        low=mid+1
                else:
                    key=Ans[mid-1]

            for i in range(len(A)):
                A[i]=A[i]/key

            if(gcd_n(A)==1):
                Z.append("YES")
            else:
                Z.append("NO")


for i in range(len(Z)):
    print Z[i]
