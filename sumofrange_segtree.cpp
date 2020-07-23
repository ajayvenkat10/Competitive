#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000005
#define ll long long
using namespace std;

ll findSubsequences(ll sequence[], ll n)
{
	unordered_map<ll, vector<ll> > dictionary;
	unordered_map<ll,ll>sum_dict;

	ll xorResult = 0;
	ll sum = 0;
	for (ll i = 0; i < n; i++)
	{
		xorResult ^= sequence[i];

		if (xorResult == 0)
			sum += i;

		if (dictionary.find(xorResult) != dictionary.end())
		{
			vector<ll> vc = dictionary[xorResult];
			sum += ((vc.size() * i) - (sum_dict[xorResult] + (vc.size()*1)));
		}
		dictionary[xorResult].push_back(i);
		sum_dict[xorResult] += i;
	}

	return sum;
}

int main()
{
	ll t;
    cin >> t;

    while(t--)
    {
    	ll arr[MAX];
        ll n;
        cin >> n;

        for(ll i = 0; i<n; i++)
            cin >> arr[i];

		ll out = findSubsequences(arr, n);
		cout<<out<<endl;
	}
	return 0;
}
