# void addEdge(vector<ll> adj[], ll u, ll v)
# {
#     adj[u].push_back(v);
#     adj[v].push_back(u);
# }
#
# void DFSUtil(ll u, vector<ll> adj[],
#              vector<bool> &visited)
# {
#     visited[u] = true;
#     dfs_order[ind++] = u;
#     for (ll i = 0; i < adj[u].size(); i++)
#         if (visited[adj[u][i]] == false)
#             DFSUtil(adj[u][i], adj, visited);
# }
#
# void DFS(vector<ll> adj[], ll V)
# {
#     vector<bool> visited(V, false);
#     for (ll u = 0; u < V; u++)
#         if (visited[u] == false)
#             DFSUtil(u, adj, visited);
# }
# from collections import defaultdict
# adj = defaultdict(list)
#
# def addEdge(u,v):
#     adj[u].append(v)
#     adj[v].append(u)
#
# def DFSUtil(u,visited):
#     visited[u] = True
#     for i in range(len(adj[u])):
#         if(not visited[adj[u][i]]):
#             DFSUtil(u,visited)
#
# def DFS(V):
#     visited = [False]*V
#     for i in range(V):
#         if(not visited[u]):
#             DFSUtil(u,visited)
#
# A = 4
#
# B = [[1,2],[2,3],[3,4]]
#
# C = [1,2,3,4]
#
# for i in range(len(B)):
#     addEdge(B[i][0], B[i][1])


def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum , lis[i])

    return maximum
# end of lis function

# Driver program to test above function
arr = [11, 49, 36, 12, 1]
print ("Length of lis is", lis(arr))
