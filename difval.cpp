#include<bits/stdc++.h> 
#include<math.h>
#define max_color 500005 
#define maxn 500005 
#define ll long long
using namespace std; 

ll bit[maxn], vis_time[maxn] = {0}, end_time[maxn] = {0}; 
ll flat_tree[maxn] = {0};  
ll depth[maxn] = {0}; 
ll tim = 0;  
set<ll>*segment; 
  
void build(ll i, ll s, ll e, ll arr[]) 
{ 
  
    if (s == e) { 
        segment[i].insert(arr[s]); 
        return; 
    } 
  
    build(2 * i, s, (s + e) / 2, arr); 
    build(1 + 2 * i, 1 + (s + e) / 2, e, arr); 
  
    segment[i].insert(segment[2 * i].begin(), 
                      segment[2 * i].end()); 
  
    segment[i].insert(segment[2 * i + 1].begin(), 
                      segment[2 * i + 1].end()); 
} 
  
set<ll> query(ll node, ll l, ll r, ll a, ll b) 
{ 
    set<ll> left, right, result; 
  
    if (b < l || a > r) 
        return result; 
  
    if (a <= l && r <= b) 
        return segment[node]; 
  
    left = query(2 * node, l, (l + r) / 2, a, b); 
    result.insert(left.begin(), left.end()); 
  
    right = query(1 + 2 * node, 1 + (l + r) / 2, r, a, b); 
    result.insert(right.begin(), right.end()); 
  
    return result; 
} 
  
void init(ll n) 
{ 
    ll h = (ll)ceil(log2(n)); 
    h = (2 * (pow(2, h))) - 1; 

    segment = new set<ll>[h]; 
} 
  
// void getDistinct(ll l, ll r, ll n) 
// { 
//     set<ll> ans = query(1, 0, n - 1, l, r); 
  
//     cout << ans.size() << endl; 
// } 

void DFSEuler(ll v, ll par, ll color[], vector<ll> tree[], ll depth1 = 0) 
{ 
	depth[v] = depth1;
  
    vis_time[v] = ++tim;  
  
    flat_tree[tim] = v; 
  
    for (ll i : tree[v]) { 
        if (i == par) 
            continue; 
  
        DFSEuler(i, v, color, tree, depth1 + 1); 
    } 
  
    end_time[v] = tim;  
} 

void addEdge(ll u, ll v, vector<ll> tree[]) 
{ 
	tree[u].push_back(v); 
	tree[v].push_back(u); 
} 

int main() 
{ 
	ll t;
	cin >> t;
	while(t--){
		ll n;
		cin >> n;

		// memset(vis_time, 0, sizeof(vis_time));
		// memset(end_time, 0, sizeof(end_time));
		// memset(depth, -1, sizeof(depth));
		
		ll nodes;
		bool flag = true;

		vector<ll> *tree = new vector<ll>[maxn];

		for(ll i=2; i<=n; i++){
			cin >> nodes;
			if(nodes == i-1)
				flag &= true;
			else
				flag &= false;

			addEdge(i, nodes, tree);
		}		

		ll color[max_color] = {0};

		color[0] = 0;

		for(ll i=1; i<=n; i++){
			cin >> color[i];
		}

		// if(flag){
		// 	init(n+1); 
    	// 	build(1, 1, n, color); 
		// }
		// else{
		// 	DFSEuler(1, 0, color, tree);
		// }

		init(n+1); 
    	build(1, 1, n, color); 

		ll q;
		cin >> q;

		ll ans = 0;

		while(q--){
			ll x,d;
			cin >> x >> d;
			
			set<ll> count;
		
			x = x ^ ans;
			d = d ^ ans;

			count = query(1, 1, n, x, min(x+d, n));
			ans = count.size();	
			// if(flag){
			// 	count = query(1, 1, n, x, min(x+d, n));
			// 	ans = count.size();	
			// }

			// else{
			// 	if(depth[x] == -1)
			// 		ans = 0;

			// 	else{
			// 		for(ll i= vis_time[x]; i<= end_time[x]; i++){
			// 			if(abs(depth[flat_tree[i]] - depth[x]) <= d){
			// 				count.insert(color[flat_tree[i]]);	
			// 			}
			// 		}	
			// 		ans = count.size();
			// 	}
			// }
			
			cout<<ans<<endl;
		}
		
		tim = 0;
	}

	return 0; 
} 
