from collections import defaultdict

t=int(input())
while(t>0):
    n=int(input())
    d = {}
    d = defaultdict(int)
    while(n>0):
        s=input()
        
        d[s]+=1
        n-=1
    arr=list(d.keys())
    l=len(arr)
    for i in range(l):
        for j in range(i+1,l):
            ans=arr[i].union(arr[j])
            print(ans)
    t-=1
