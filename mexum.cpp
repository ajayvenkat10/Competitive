#include <bits/stdc++.h>

typedef unsigned long long ll;
typedef unsigned long long ull;

#define mod 998244353

using namespace std;

int main()
{
	vector<ull> pow2(100005);

	pow2[0] = 1;
	for (ull i = 1; i < 100005; i++)
		pow2[i] = pow2[i - 1] * 2 % mod;

	map<ull, ull> arr;

	ull t;

	cin >> t;

	while (t--)
	{
		ull n;
		ull input;
		ull prod = 1;
		ull ans = 0;
		cin >> n;

		map<ull, ull> freq_of_elem;

		for (ull i = 0; i < n; i++)
		{
			cin >> input;

			if (input >= n + 1)
				freq_of_elem[n + 1]++;
			else
				freq_of_elem[input]++;
		}

		// Iterating for aull mex values --- //
		ull total = 0;
		for (ull i = 1;i <= n + 1;i++)
		{
			total += freq_of_elem[i];

			// ans = (((ans) + pow2[n - total] * i % mod ) * prod) % mod;
            cout<<"prod: "<<prod<<endl;
			ans = (ans + (pow2[n - total] * i % mod) * prod) % mod;
			prod = prod * (pow2[freq_of_elem[i]] - 1 + mod) % mod;
            cout<<"ans: "<<ans<<endl;
			// prod = prod * (pow2[freq_of_elem[i]] - 1 + mod) % mod;
		}
		
		cout << ans << "\n";
	}
}
