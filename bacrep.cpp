#include <bits/stdc++.h>
#define ll long long
#define MAX 500000
using namespace std;

//Initializing global varaibles and vectors

ll maximumHeight = 0;
ll queryTime = 0;
ll results_index = 0;
ll segmentTreeSize = 0;

vector<ll> segmentTree;
vector<bool> isLeaf(MAX, true);
vector<ll> depth(MAX);
vector<ll> results(MAX);
vector<ll> adjacencyList[MAX];
vector<pair<ll, ll>> updates[MAX];
vector<pair<ll, ll>> queries[MAX];

//Range update on segment tree
void update(ll node, ll left, ll right, ll position, ll value)
{

    if (left == right)
    {
        segmentTree[node] += value;
        return;
    }

    ll mid = (left + right) / 2;

    if (position <= mid)
        update(2 * node, left, mid, position, value);

    else
        update(2 * node + 1, mid + 1, right, position, value);

    segmentTree[node] = segmentTree[2 * node] + segmentTree[2 * node + 1];
}

//Querying segment tree
ll query(ll node, ll left, ll right, ll start, ll end)
{

    if (start > right || end < left)
        return 0;

    if (start <= left && end >= right)
        return segmentTree[node];

    ll mid = (left + right) / 2;

    ll partOne = query(2 * node, left, mid, start, end);
    ll partTwo = query(2 * node + 1, mid + 1, right, start, end);

    return (partOne + partTwo);
}

//Modified Depth First Search
void depthFirstSearch(ll node, ll parentNode)
{
    for (auto connectedNode : adjacencyList[node])
    {
        if (connectedNode != parentNode)
        {
            isLeaf[node] = false;
            depth[connectedNode] = depth[node] + 1;
            maximumHeight = max(maximumHeight, depth[connectedNode]);
            depthFirstSearch(connectedNode, node);
        }
    }
}

//Processing all the queries for each node
void processAllQueries(ll node, ll parentNode)
{

    for (auto updateQuery : updates[node])
    {
        update(1, 0, segmentTreeSize, updateQuery.first, updateQuery.second);
    }

    for (auto pointQuery : queries[node])
    {
        if (isLeaf[node])
            results[pointQuery.second] = query(1, 0, segmentTreeSize, 0, pointQuery.first);
        else
            results[pointQuery.second] = query(1, 0, segmentTreeSize, pointQuery.first, pointQuery.first);
    }

    for (auto connectedNode : adjacencyList[node])
    {
        if (connectedNode != parentNode)
            processAllQueries(connectedNode, node);
    }

    for (auto updateQuery : updates[node])
    {
        update(1, 0, segmentTreeSize, updateQuery.first, -updateQuery.second);
    }
}

void addEdge(ll u, ll v)
{
    adjacencyList[u].push_back(v);
    adjacencyList[v].push_back(u);
}

int main()
{
    ll N, Q;
    cin >> N >> Q;
    ll V = N;
    V -= 1;

    while (V--)
    {
        ll u, v;
        cin >> u >> v;
        addEdge(u, v);
    }

    depthFirstSearch(1, 0);

    segmentTreeSize = maximumHeight + Q;
    segmentTree.resize(segmentTreeSize << 2, 0);

    ll bacteria;

    for (ll i = 1; i <= N; i++)
    {
        cin >> bacteria;
        updates[i].push_back(make_pair(maximumHeight - depth[i], bacteria));
    }

    char operation;

    while (Q--)
    {
        queryTime++;

        cin >> operation;
        ll node, bacteriaToBeAdded;

        if (operation == '+')
        {
            cin >> node >> bacteriaToBeAdded;
            updates[node].push_back(make_pair(maximumHeight + queryTime - depth[node], bacteriaToBeAdded));
        }

        else
        {
            cin >> node;
            queries[node].push_back(make_pair(maximumHeight + queryTime - depth[node], results_index++));
        }
    }

    processAllQueries(1, 0);

    for (ll i = 0; i < results_index; i++)
    {
        cout << results[i] << endl;
    }

    return 0;
}
