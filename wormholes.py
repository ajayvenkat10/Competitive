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
mid1=(len(W)-1)//2
X=[]
Y=[]
Z=[]
mid=0
for i in range(len(start_time)):
    mid=(len(V)-1)/2
    while(mid>=0 and mid<=len(V)-1):
        if(V[mid]>start_time[i]):
            if(mid==0):
                X.append(V[mid])
                break
            elif(V[mid-1]<=start_time[i]):
                X.append(V[mid-1])
                break
            else:
                mid=mid-1

        elif(V[mid]==start_time[i]):
            X.append(V[mid])
            break

        else:
            mid=mid+1
            if(mid==len(V)):
                X.append(-1)

for i in range(len(exit_time)):
    mid1=(len(W)-1)/2
    while(mid1>=0 and mid1<=len(W)-1):
        if(exit_time[i]==W[mid1]):
            Y.append(W[mid1])
            break
        elif(W[mid1]>=exit_time[i]):
            if(mid1==0):
                Y.append(W[mid1])
                break
            elif(W[mid1-1]<exit_time[i]):
                Y.append(W[mid1])
                break
            else:
                mid1=mid1-1
        else:
            mid1=mid1+1
            if(mid1==len(W)):
                Y.append(-1)

for i in range(len(start_time)-1):
    if(X[i]==-1 or Y[i]==-1):
        continue
    else:
        r=(Y[i]-X[i])+1
        Z.append(r)

Z=mergesort(Z)
print Z[0]
