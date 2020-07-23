t = int(input())
j = 0
for i in range(t):
    j += 1
    n,m = map(int,input().split())
    for i in range(m):
        node1,node2 = map(int,input().split())

    print("Case #%d: %d" % (j , m + ((n-1)-m)*2))

    
