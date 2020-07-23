#include <bits/stdc++.h>
#define ll long long
#define MAX 100005
using namespace std;

struct node
{
	ll first;
	ll second;
};

node segtree[4 * MAX];
ll arr[MAX];

void build(ll index, ll start, ll end)
{
	if (start == end)
	{
		segtree[index].first = arr[start];
		segtree[index].second = -1;
		return;
	}

	ll mid = (start + end) / 2;
	build(2 * index + 1, start, mid);
	build(2 * index + 2, mid + 1, end);

	segtree[index].first = max(segtree[2 * index + 1].first, segtree[2 * index + 2].first);
	segtree[index].second = min(max(segtree[2 * index + 1].first, segtree[2 * index + 2].second),
								max(segtree[2 * index + 1].second, segtree[2 * index + 2].first));
}

node query(ll index, ll start, ll end, ll L, ll R)
{
	node result;
	result.first = -1;
	result.second = -1;

	if (start > R || end < L)
		return result;

	if (start >= L && end <= R)
		return segtree[index];

	ll mid = (start + end) / 2;

	node left = query(2 * index + 1, start, mid, L, R);
	node right = query(2 * index + 2, mid + 1, end, L, R);

	result.first = max(left.first, right.first);
	result.second = min(max(left.first, right.second), max(left.second, right.first));
	return result;
}

void update(ll index, ll start, ll end, ll idx, ll value)
{
	if (start == end)
	{
		segtree[index].first = value;
		segtree[index].second = -1;
		return;
	}

	else
	{
		ll mid = (start + end) / 2;

		if (idx <= mid)
			update(2 * index + 1, start, mid, idx, value);
		else
			update(2 * index + 2, mid + 1, end, idx, value);

		segtree[index].first = max(segtree[2 * index + 1].first, segtree[2 * index + 2].first);
		segtree[index].second = min(max(segtree[2 * index + 1].first, segtree[2 * index + 2].second),
									max(segtree[2 * index + 1].second, segtree[2 * index + 2].first));
	}
}

int main()
{
	ll n, q;
	char operation;

	cin >> n;
	for (ll i = 0; i < n; i++)
		cin >> arr[i];

	build(0, 0, n - 1);
	cin >> q;

	for (ll i = 0; i < q; i++)
	{
		ll x, y;
		cin >> operation >> x >> y;

		if (operation == 'Q')
		{
			node result = query(0, 0, n - 1, x - 1, y - 1);
			cout << result.first + result.second << endl;
		}

		else
			update(0, 0, n - 1, x - 1, y);
	}

	return 0;
}
