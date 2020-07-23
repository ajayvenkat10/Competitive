n=int(input())
N=input()
N = N.split()
A = []
for i in range(n):
    a = int(N[i])
    A.append(a)
max2=0
live=0
pos=0
start=0
max_start=0
stack=0
max1=0
current=0
for i in range(n):
    if (A[i]==1):
        stack=stack+1
    else:
        if(max2<stack):
            max2=stack
            pos=i

        stack=stack-1
        if(stack==0):
            if(i-start>max1):
                max1=i-start+1
                max_start=start+1
            start=i+1

print(max2,pos,max1,max_start)
