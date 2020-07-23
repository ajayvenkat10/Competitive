def dfs(node,p):
    sum = tree_elements[node]
    for pos in connect[node]:
        if(pos!=p):
            sum += dfs(pos,node)
    sum = max(sum,-x)
    return(sum)

t = int(input())
for i in range(t):
    line = input().split()
    n,x  = int(line[0]),int(line[1])

    tree_elements = []
    line1 = input().split()
    for i in range(n):
        tree_elements.append(int(line1[i]))

    connect = []
    for i in range(n):
        connect.append([])

    for i in range(n-1):
        edges = input().split()
        u,v = int(edges[0]),int(edges[1])
        u -= 1
        v -= 1
        connect[u].append(v)
        connect[v].append(u)

    ans = dfs(0,-1)
    print(ans)
