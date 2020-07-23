import sys
def mergesort(A):
    if(len(A)==1):
        return A
    arr1= mergesort(A[0:len(A)/2])
    arr2= mergesort(A[len(A)/2:])
    return merge(arr1,arr2)

def merge(a,b):
    i=0
    j=0
    O=[]
    while(i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            O.append(a[i])
            i=i+1
        else:
            O.append(b[j])
            j=j+1
    if(i==len(a)):
        O.extend(b[j:])
    else:
        O.extend(a[i:])
    return O


N=raw_input(" ")
N=N.split(" ")
contest=int(N[0])
enter=int(N[1])
exit=int(N[2])

start_time=[]
exit_time=[]
V=[]
W=[]
for i in range(contest):
    contest_time =raw_input("")
    contest_time=contest_time.split(" ")
    s=int(contest_time[0])
    start_time.append(s)
    e=int(contest_time[1])
    exit_time.append(e)

a=raw_input("")
a=a.split(" ")
for i in range(enter):
    n=int(a[i])
    V.append(n)

b=raw_input("")
b=b.split(" ")
for i in range(exit):
    m=int(b[i])
    W.append(m)

V=mergesort(V)
W=mergesort(W)
mid1=0
low1=0
high1=len(W)-1
X=[]
Y=[]
Z=[]
count=0
mid=0
low=0
high=len(V)-1
for i in range(len(start_time)):
    low=0
    high=len(V)-1
    mid=(low+high)/2
    while(low<=high):
        mid=(low+high)/2
        if(V[mid]<start_time[i]):
            if(mid!=len(V)-1):
                if(V[mid+1]==start_time[i]):
                    X.append(V[mid+1])
                    count=count+1
                    break
                elif(V[mid+1]>start_time[i]):
                    X.append(V[mid])
                    count=count+1
                    break
                else:
                    low=mid+1
            else:
                X.append(V[mid])
                count=count+1
                break

        elif(V[mid]==start_time[i]):
            X.append(V[mid])
            count=count+1
            break

        else:
            high=mid-1

    if(count==0):
        X.append(-1)
    count=0

for i in range(len(exit_time)):
    low1=0
    high1=len(W)-1
    mid1=(low1+high1)/2
    while(low1<=high1):
        mid1=(low1+high1)/2
        if(exit_time[i]==W[mid1]):
            Y.append(W[mid1])
            count=count+1
            break

        elif(W[mid1]>exit_time[i]):
            if(mid1!=0):
                if(W[mid1-1]==exit_time[i]):
                    Y.append(W[mid1-1])
                    count=count+1
                    break
                elif(W[mid1-1]<exit_time[i]):
                    Y.append(W[mid1])
                    count=count+1
                    break
                else:
                    high1=mid1-1
            else:
                Y.append(W[mid1])
                count=count+1
                break

        else:
            low1=mid1+1

    if(count==0):
        Y.append(-1)
    count=0


if(len(start_time)==1 and len(exit_time)==1):
    if(X[0]==-1 or Y[0]==-1):
        sys.exit()
    else:
        r=(Y[0]-X[0])+1
        print r
else:
    for i in range(len(start_time)):
        if(X[i]==-1 or Y[i]==-1):
            continue
        else:
            r=(Y[i]-X[i])+1
            Z.append(r)
    if not Z:
        sys.exit()
    else:
        Z=mergesort(Z)
        print Z[0]
