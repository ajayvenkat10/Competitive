n=int(raw_input(""))
N=raw_input("")
N = N.split(" ")
A = []
for i in range(n):
    a = int(N[i])
    A.append(a)
if (len(A)<2 or len(A)>10**5):
    quit()
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
        live=live+1
        stack=stack+1
    if (A[i]==2):
        if (max2<live):
            max2=live
            pos=i
        live=0
        stack=stack-1
        if(stack==0):
            if(i-start>max1):
                max1=i-start+1
                max_start=start+1
            start=i+1

print "%d %d %d %d" % (max2,pos,max1,max_start)
