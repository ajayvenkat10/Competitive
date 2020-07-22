#include <bits/stdc++.h> 
#define ll long long
using namespace std; 
#define MAXN 100005
#define MAXAI 1000005 
#define MOD 1000000007
#define level 18 

vector <ll> tree[MAXN];
ll product_arr[MAXN] = {1}; 
ll depth[MAXN]; 
ll parent[MAXN][level]; 
bool vis[MAXN];
ll number_of_factors;
ll gp[MAXAI];
map<ll,ll>factors_map_of_all[MAXAI];
map<ll,ll> product_factors[MAXN];
map<ll,ll>product_factors_dup[MAXN];

struct primeFactorization
{
    ll countOfPf, primeFactor;
};

void populateProductTreeFactors(ll n, ll position){
    ll count,p;
    while(n > 1)
    {
        count = 0;
        p = gp[n];
        while(n%p == 0)
        {
            n /= p;
            count++;
        }

        factors_map_of_all[position][p] = count;
        // product_factors[position][p]= count;
        // product_factors_dup[position][p] = count;
    }
}

void bfs(ll node) 
{ 
  
    // Create a queue of {child, parent} 
    queue<pair<ll, ll> > qu; 
  
    // Push root node in the front of 
    qu.push({ node, 1 }); 
  
    while (!qu.empty()) { 
        pair<ll, ll> p = qu.front(); 
  
        // Dequeue a vertex from queue 
        qu.pop(); 

        if(p.first != p.second){
            for(auto it : product_factors_dup[p.first]){
                product_factors_dup[p.first][it.first] += product_factors_dup[p.second][it.first];
            }
            product_factors_dup[p.first].insert(product_factors_dup[p.second].begin(), product_factors_dup[p.second].end());
        }
    
        vis[p.first] = true; 
        
        for (ll child : tree[p.first]) { 
            if (!vis[child]) { 
                qu.push({ child, p.first }); 
            } 
        } 
    } 
} 

void dfs(ll cur, ll prev) 
{ 
	depth[cur] = depth[prev] + 1; 
	parent[cur][0] = prev; 
	for (ll i=0; i<tree[cur].size(); i++) 
	{ 
		if (tree[cur][i] != prev) 
			dfs(tree[cur][i], cur); 
	} 
} 

void precomputeSparseMatrix(ll n) 
{ 
	for (ll i=1; i<level; i++) 
	{ 
		for (ll node = 1; node <= n; node++) 
		{ 
			if (parent[node][i-1] != -1) 
				parent[node][i] = 
					parent[parent[node][i-1]][i-1]; 
		} 
	} 
} 

ll lca(ll u, ll v) 
{ 
	if (depth[v] < depth[u]) 
		swap(u, v); 

	ll diff = depth[v] - depth[u]; 

	// Step 1 of the pseudocode 
	for (ll i=0; i<level; i++) 
		if ((diff>>i)&1) 
			v = parent[v][i]; 

	// now depth[u] == depth[v] 
	if (u == v) 
		return u; 

	// Step 2 of the pseudocode 
	for (ll i=level-1; i>=0; i--) 
		if (parent[u][i] != parent[v][i]) 
		{ 
			u = parent[u][i]; 
			v = parent[v][i]; 
		} 

	return parent[u][0]; 
} 

void addEdge(ll u,ll v) 
{ 
tree[u].push_back(v); 
	tree[v].push_back(u); 
} 

void generateAllPrimes(){
    for (ll i = 0; i <= MAXAI; i++)
        gp[i] = 0;

    for (ll i = 2; i <= MAXAI; i++)
{
        if (!gp[i])
        {
            for (ll j = i; j <= MAXAI; j += i)
                gp[j] = i;
        }
    }
}

// driver function 
int main() 
{ 
	memset(parent,-1,sizeof(parent)); 

    ll t;
    cin >> t;

    generateAllPrimes();
    
    for(ll i=1; i<MAXAI; i++){
        populateProductTreeFactors(i,i);
    } 

    while(t--){

        ll N,Q;
        ll u,v;
        ll root = 1;
        cin>>N;

        for(ll i=0; i<N-1; i++){
            cin>>u>>v;
            addEdge(u,v);
        }

        depth[0] = 0; 

	    // dfs(1,0);    

	    // precomputeSparseMatrix(N);

        for(ll i=1; i<=N; i++){
            cin>>product_arr[i];
            product_factors_dup[i].clear();
            product_factors_dup[i].insert(factors_map_of_all[product_arr[i]].begin(), factors_map_of_all[product_arr[i]].end());
        }

        bfs(1);

        cin>>Q;

        while(Q--){
            ll product;
            ll start, end;
            cin>>start>>end;

            // ll lowest_common_ancestor = lca(start,end);
    
            number_of_factors = 1;

            // map<ll,ll>answer_map;
            
            // answer_map.insert(product_factors_dup[start].begin(), product_factors_dup[start].end());
            // answer_map.insert(product_factors_dup[end].begin(), product_factors_dup[end].end());
            
            // if(lowest_common_ancestor == root){
            
            //     for (auto it: answer_map){
            //         answer_map[it.first] = product_factors_dup[start][it.first] + product_factors_dup[end][it.first] - 
            //                                 product_factors_dup[lowest_common_ancestor][it.first];

            //         number_of_factors *= (answer_map[it.first]+1) % MOD;
            //     }

            // }

            // else{
            //         for (auto it: answer_map){
            //         answer_map[it.first] = product_factors_dup[start][it.first] + product_factors_dup[end][it.first] - 
            //                                 ((product_factors_dup[lowest_common_ancestor][it.first] * 2) - 
            //                                 factors_map_of_all[product_arr[lowest_common_ancestor]][it.first]);

            //         number_of_factors *= (answer_map[it.first]+1) % MOD;
            //      }
            // }

            cout<<number_of_factors % MOD<<endl;

        }
    }
    
	return 0; 
} 
