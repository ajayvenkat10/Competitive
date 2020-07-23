#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll arr[500000] = {0};
ll ind = 0;
ll dfs_order[500000] = {0};
ll ind_arr[500000] = {0};

void addEdge(vector<ll> adj[], ll u, ll v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void DFSUtil(ll u, vector<ll> adj[],
             vector<bool> &visited)
{
    visited[u] = true;
    dfs_order[ind++] = u;
    for (ll i = 0; i < adj[u].size(); i++)
        if (visited[adj[u][i]] == false)
            DFSUtil(adj[u][i], adj, visited);
}

void DFS(vector<ll> adj[], ll V)
{
    vector<bool> visited(V, false);
    for (ll u = 0; u < V; u++)
        if (visited[u] == false)
            DFSUtil(u, adj, visited);
}

int main()
{
    ll N, Q;
    cin >> N >> Q;
    vector<ll> *adj = new vector<ll>[N];
    ll V = N;
    V -= 1;

    while (V--)
    {
        ll u, v;
        cin >> u >> v;
        addEdge(adj, u - 1, v - 1);
    }
    DFS(adj, N);

    for (ll i = 0; i < N; i++)
        cin >> arr[i];

    for (ll i = 0; i < N; i++)
        ind_arr[dfs_order[i]] = i;

    char operation;

    while (Q--)
    {
        for (ll i = N - 1; i >= 0; i--)
        {
            ll count = 0;
            for (auto it = adj[dfs_order[i]].begin(); it!= adj[dfs_order[i]].end(); it++)
            {
                if (ind_arr[*it] > ind_arr[dfs_order[i]])
                {
                    arr[*it] += arr[dfs_order[i]];
                    count++;
                }
            }
            if (count)
                arr[dfs_order[i]] = 0;
        }

        cin >> operation;
        ll x, val;
        if (operation == '+')
        {
            cin >> x >> val;
            arr[x - 1] += val;
        }

        else
        {
            cin >> x;
            cout << arr[x - 1] << endl;
        }

    }

    return 0;
}
