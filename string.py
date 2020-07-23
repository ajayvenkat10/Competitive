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

n=int(raw_input(""))
Z=[]
for i in range(n):
    s=raw_input("")
    s=mergesort(s)
    q=set(s)
    q=list(q)
    X=[]
    count=0
    count1=0
    for i in range(len(q)):
        x=q[i]
        count=0
        for i in range(len(s)):
            if(x==s[i]):
                count =count+1
        X.append(count)

    X.sort()
    num=X[len(X)-1]
    for i in range(len(X)-1):
        for j in range(1,len(X)-1):
            if(X[i]+X[j]==num):
                count1=1
    if(count1==1):
        Z.append("Dynamic")
    else:
        Z.append("Not")

for i in range(len(Z)):
    print Z[i]
