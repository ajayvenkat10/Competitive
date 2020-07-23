n=int(raw_input(""))
A=[]
a=raw_input("")
a=a.split()

for i in range(n):
    A.append(long(a[i]))

A.sort()
A=A[::-1]

i=0
sum=0
for i in range(n):
    sum=sum+A[i]

final=0
x=0
y=0
i=0
for i in range(len(A)-1):
    x= A[i]*(n-1-i)
    sum=sum-A[i]
    final= final+(x-sum)

print final
