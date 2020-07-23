from collections import defaultdict

t = int(input())

for _ in range(t):
    nodes,edges = map(int, input().split())
    connected = defaultdict(list)
    degrees = defaultdict(int)

    for i in range(edges):
        u,v = map(int, input().split())
        u-=1
        v-=1

        degrees[u] += 1
        degrees[v] += 1
        connected[u].append(v)
        connected[v].append(u)

    subgraph = [1]*nodes

    if(edges%2==0):
        k = 1
        print(k)
        print(*subgraph)

    else:
        flag = 0
        pos = -1

        for i in range(nodes):
            if(degrees[i]%2 == 1):
                pos = i
                flag = 1
                break

        if(flag):
            k = 2
            subgraph[pos] = 2


        else:
            k = 3
            for i in range(nodes):
                if(degrees[i] > 0):
                    index1 = i
                    break

            index2 = connected[index1][0]
            subgraph[index1] = 2
            subgraph[index2] = 3

        print(k)
        print(*subgraph)
