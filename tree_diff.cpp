// #include <bits/stdc++.h>
// #define ll long long
// #define MAX 100005

// using namespace std;

// int value[MAX]={0};
// int ans[MAX]={0};
// int total = 0;

// void addEdge(vector<int> v[],
//              int x,
//              int y)
// {
//     v[x].push_back(y);
//     v[y].push_back(x);
// }

// void printPath(vector<int> stack) 
// { 
//     vector<int> ans;
//     int i; 
//     for (i = 0; i < (int)stack.size() - 1; i++) {
//         ans[total++] = value[stack[i]];
//     } 
//     ans[total++] = value[stack[i]];
// }

// void DFS(vector<int> v[],
//          bool vis[],
//          int x,
//          int y,
//          vector<int> stack)
// {
//     stack.push_back(x);
//     if (x == y)
//     {
//         printPath(stack);
//         return;
//     }
//     vis[x] = true;

//     int flag = 0;
//     if (!v[x].empty())
//     {
//         for (int j = 0; j < v[x].size(); j++)
//         {
//             if (vis[v[x][j]] == false)
//             {
//                 DFS(v, vis, v[x][j], y, stack);
//                 flag = 1;
//             }
//         }
//     }
//     if (flag == 0)
//     {
//         stack.pop_back();
//     }
// }

// void DFSCall(int x,
//              int y,
//              vector<int> v[],
//              int n,
//              vector<int> stack)
// {

//     bool vis[n + 1];

//     memset(vis, false, sizeof(vis));

//     DFS(v, vis, x, y, stack);
// }

// int main()
// {
//     int t;
//     cin>>t;

//     while(t--){
//         int n, q,u,v;
//         cin>>n>>q;

//         vector<int> tree[n], stack;

//         for(int i=0; i<n; i++)
//             cin>>value[i];

//         for(int i=0; i<n-1; i++){
//             cin>>u>>v;
//             addEdge(tree,u,v);
//         }

//         while(q--){
//             int start, end;
//             cin>>start,end;

//             DFSCall(start,end,tree,n,stack);

//             sort(ans,ans+ total, greater<int>());

//             int mini = MAX;

//             for(int i =1; i<total; i++){
//                 if(abs(ans[i-1] - ans[i]) < mini)
//                     mini =  abs(ans[i-1] - ans[i]);
//             }

//             cout<<mini<<endl;

//             total = 0;
//         }
//     }

//     return 0;
// }


// C++ implementation 
#include <bits/stdc++.h> 
using namespace std; 

int arr[100005] = {0};
int total = 0;
int value [100005]={0};

// An utility function to add an edge in an 
// undirected graph. 
void addEdge(vector<int> v[], 
			int x, 
			int y) 
{ 
	v[x].push_back(y); 
	v[y].push_back(x); 
} 

// A function to print the path between 
// the given pair of nodes. 
void printPath(vector<int> stack) 
{ 
	int i; 
	for (i = 0; i < (int)stack.size() - 1; 
		i++) { 
		// cout << stack[i] << " -> ";
        arr[total] = stack[i]; 
        total++;
	} 
	arr[total] = stack[i];
    total++;
} 

// An utility function to do 
// DFS of graph recursively 
// from a given vertex x. 
void DFS(vector<int> v[], 
		bool vis[], 
		int x, 
		int y, 
		vector<int> stack) 
{ 
	stack.push_back(x); 
	if (x == y) { 

		// print the path and return on 
		// reaching the destination node 
		printPath(stack); 
		return; 
	} 
	vis[x] = true; 

	// A flag variable to keep track 
	// if backtracking is taking place 
	int flag = 0; 
	if (!v[x].empty()) { 
		for (int j = 0; j < v[x].size(); j++) { 
			// if the node is not visited 
			if (vis[v[x][j]] == false) { 
				DFS(v, vis, v[x][j], y, stack); 
				flag = 1; 
			} 
		} 
	} 
	if (flag == 0) { 

		// If backtracking is taking 
		// place then pop 
		stack.pop_back(); 
	} 
} 

// A utility function to initialise 
// visited for the node and call 
// DFS function for a given vertex x. 
void DFSCall(int x, 
			int y, 
			vector<int> v[], 
			int n, 
			vector<int> stack) 
{ 
	// visited array 
	bool vis[n + 1]; 

	memset(vis, false, sizeof(vis)); 

	// DFS function call 
	DFS(v, vis, x, y, stack); 
} 

// Driver Code 
int main() 
{ 
	
    int t;
    cin>>t;

    while(t--){
        int n,q;
        cin>>n>>q;

        vector<int> v[n], stack; 

        for(int i=1; i<=n; i++)
            cin>>value[i];

        for(int i=0; i<n-1; i++){
            int a,b;
            cin>>a>>b;
            addEdge(v,a,b);
        } 

        while(q--){
            int start,end;

            cin>>start,end;

            DFSCall(start, end, v, n, stack); 

            // Function Call 

            for(int i=0; i<total; i++){
                cout<<arr[i]<<" ";
            }
            cout<<endl;
            return 0; 
        }  
    }
	
} 
