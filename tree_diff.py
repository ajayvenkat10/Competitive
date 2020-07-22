
def bfs(length):
        queue = [1]* (length+1)
        pos = 1
        level[1] = 0
        while pos >= 1:
            pushed_node = queue[pos]
            pos -= 1
            depth = level[pushed_node] + 1
            for node in tree[pushed_node]:
                if level[node] == -1:
                    level[node] = depth
                    parent[node] = pushed_node
                    pos += 1
                    queue[pos] = node

def addEdge(first, second):
    tree[first].append(second)
    tree[second].append(first)


def treeDiff(node_a, node_b):
    frequency = [0]*101

    while(node_a != node_b):
        if(level[node_a] > level[node_b]):
            if(frequency[value[node_a]] == 1):
                return 0
            frequency[value[node_a]] += 1
            node_a = parent[node_a]

        else:
            if(frequency[value[node_b]] == 1):
                return 0
            frequency[value[node_b]] += 1
            node_b = parent[node_b]

    if(frequency[value[node_a]] == 1):
        return 0
    frequency[value[node_a]] += 1

    diff = 101
    previous = -101
    for i in range(1, 101):
        if(frequency[i] == 1):
            diff = min(diff, i-previous)
            previous = i

    return diff


t = int(input())

for i in range(t):
    n, q = map(int, input().split())
    value = list(map(int, input().split()))
    value.insert(0, -1)

    tree = []

    for i in range(n+1):
        tree.append([])

    parent = [0]*(n+1)
    level = [-1]*(n+1)

    for i in range(n-1):
        u, v = map(int, input().split())
        addEdge(u, v)

    bfs(n)

    for i in range(q):
        u, v = map(int, input().split())

        print(treeDiff(u, v))
