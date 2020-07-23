n=int(input(""))
A=[]
C=[]
sum=0
sum1=0
for i in range(n):
    a=int(input(""))
    A.append(a)

A.sort()
for i in range(n):
    sum= A[i]*(n-i)
    if(sum>sum1):
        sum1 = sum

print(sum1)
