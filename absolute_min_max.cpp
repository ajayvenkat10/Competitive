#include <bits/stdc++.h>
#define ll long long
#define MAX 250002

using namespace std;

ll n;
ll arr[MAX];

struct binaryIndexedTree
{

    ll size;
    ll BITree[MAX];

    void init(ll sz)
    {
        size = sz + 2;
        BITree[MAX] = {0};
    }

    void update(ll idx, ll value)
    {
        for (idx = idx + 1; idx <= size; idx += (idx & -idx))
        {
            BITree[idx] += value;
        }
    }

    ll query(ll idx)
    {
        ll query_result = 0;
        for (idx = idx + 1; idx >= 1; idx -= (idx & -idx))
        {
            query_result += BITree[idx];
        }
        return query_result;
    }

    ll LRquery(ll left, ll right)
    {
        return query(right) - query(left - 1);
    }
};

ll countOfSubarrays()
{

    vector<ll> li[MAX];
    vector<ll> stack;
    binaryIndexedTree tree_object;

    for (ll i = 0; i < n; i++)
    {
        li[i].clear();
    }

    tree_object.init(n);

    for (ll i = 0; i < n; i++)
    {
        while (!stack.empty() && arr[stack.back()] <= arr[i])
        {
            stack.pop_back();
        }

        if (stack.empty())
            tree_object.update(i, 1);

        else
            li[stack.back()].push_back(i);

        stack.push_back(i);
    }

    stack.clear();

    ll next_greatest[MAX] = {0};

    for (ll i = n - 1; i >= 0; i--)
    {
        while (!stack.empty() && arr[stack.back()] >= arr[i])
        {
            stack.pop_back();
        }

        if (stack.empty())
            next_greatest[i] = n;

        else
            next_greatest[i] = stack.back();

        stack.push_back(i);
    }

    ll valid_subarrays = 0;

    for (ll i = 0; i < n; i++)
    {
        for (ll j : li[i])
            tree_object.update(j, 1);

        valid_subarrays += tree_object.LRquery(i, next_greatest[i] - 1);
        tree_object.update(i, -1);
    }

    return valid_subarrays;
}

int main()
{
    ll t;
    cin >> t;

    while (t--)
    {
        cin >> n;

        for (ll i = 0; i < n; i++)
            cin >> arr[i];

        ll answer = 0;
        answer += countOfSubarrays();
        reverse(arr, arr + n);
        answer += countOfSubarrays();

        ll duplicate_count = 1;

        for (ll i = 1; i < n; i++)
        {
            if (arr[i] != arr[i - 1])
            {
                answer -= (duplicate_count * (duplicate_count + 1)) / 2;
                duplicate_count = 1;
            }
            else
                duplicate_count++;
        }

        answer -= (duplicate_count * (duplicate_count + 1)) / 2;

        cout << answer << endl;
    }
    return 0;
}