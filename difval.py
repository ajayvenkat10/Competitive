tim = 0
etim = 0
def DFSEuler(v, par, depth1 = 0):
    global tim 

    depth[v] = depth1

    tim += 1
    visited_time[v] = tim
  
    flat_tree[tim] = color[v]
  
    for i in tree[v]: 
        if (i == par):
            continue
        
        DFSEuler(i, v, depth1 + 1)
  
    end_time[v] = tim

# def DFSUtil(s, visited): 
          
#         global tim 
#         global etim
#         stack = [] 
      
#         stack.append(s)  
      
#         while (len(stack) != 0): 
#             etim += 1
#             s = stack[-1]
      
#             if (not visited[s]): 
#                 tim += 1
#                 visited_time[s] = tim 
#                 flat_tree[tim] = s
#                 visited[s] = True
      
#             i = len(tree[s])-1
#             while i >= 0: 
#                 if (not visited[tree[s][i]]):  
#                     stack.append(tree[s][i]) 
#                 i -= 1
         

# def DFS(n): 
#     visited = [False] * (n+1) 
#     for i in range(1,n+1): 
#         if (not visited[i]): 
#             DFSUtil(i, visited) 
            
def addEdge(first, second):
    tree[first].append(second)
    tree[second].append(first)

t = int(input())

for i in range(t):
    n = int(input())
    value = list(map(int, input().split()))
    value.insert(0, -1)
    value.insert(1, 0)

    visited_time  = [0] * (n+1) 
    end_time = [0] * (n+1)
    flat_tree = [0]* (n+1)

    tree = []

    for i in range(n+1):
        tree.append([])

    parent = [0]*(n+1)
    depth = [-1]*(n+1)

    for i in range(2, n+1):
        addEdge(i, value[i])

    color = list(map(int, input().split()))
    color.insert(0,0)

    # DFSEuler(1, 0)

    q = int(input())
    ans = 0

    for _ in range(q):
        x,d = map(int, input().split())
        x ^= ans 
        d ^= ans

        ans = len(set(color[x:x+d+1]))
        # distinct = set()
        # for i in range(visited_time[x], end_time[x]+1):
        #     if(abs(depth[flat_tree[i]] - depth[x]) <= d):
        #         distinct.add(color[flat_tree[i]])

        # ans = len(distinct)

        print(ans)
    
    tim = 0


