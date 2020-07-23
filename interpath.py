from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def printAllPathsUtil(self, u, d, visited, path):

		visited[u]= True
		path.append(u)

		if u ==d:
			return(path)
		else:
			for i in self.graph[u]:
				if visited[i]==False:
					self.printAllPathsUtil(i, d, visited, path)

		path.pop()
		visited[u]= False

	def printAllPaths(self,s, d):
		visited =[False]*(self.V)
		path = []
		self.printAllPathsUtil(s, d,visited, path)

t = int(input())

for i in range(t):
    N,Q = map(int,input().split())
    total_paths = []
    for i in range(N-1):
        start,end = map(int,input().split())
        start,end = start-1,end-1
        total_paths.append((start,end))
        total_paths.append((end,start))

    queries = []
    for i in range(Q):
        start,end = map(int,input().split())
        start,end = start-1,end-1
        queries.append((start,end))


    g = Graph(N)

    for i in range(len(total_paths)):
        g.addEdge(total_paths[i][0],total_paths[i][1])

    all_paths = []
    for i in range(N):
        for j in range(N):
            x = g.printAllPaths(i, j)
            print(x)
            all_paths.append(x)

    # print(all_paths)
    for i in range(len(queries)):
        count = 0
        query_path = g.printAllPaths(queries[i][0],queries[i][1])

        for j in range(len(all_paths)):
            if(len(all_paths[i] & query_path) == 1):
                count += 1

        print(count)




# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(0, 3)
# g.addEdge(1, 4)
# g.addEdge(1, 5)
# g.addEdge(5, 1)
# g.addEdge(4, 1)
# g.addEdge(3, 0)
# g.addEdge(2, 0)
# g.addEdge(1, 0)
