#include <bits/stdc++.h>
#define ll long long
#define MAX 200005

using namespace std;

int main()
{

    ll t;
    cin >> t;

    while (t--)
    {

        ll n, k;
        ll arr[MAX];
        cin >> n >> k;

        ll odd_count = 0;
        bool ans = true;

        for (ll i = 0; i < n; i++)
        {
            cin >> arr[i];
            if (arr[i] % 2 == 1)
                odd_count++;
        }

        vector<ll> positions;

        if (k > odd_count || (odd_count - k) % 2 == 1)
            ans = false;

        else
        {

            ll i = 0;
            while (k > 1)
            {
                if (arr[i] % 2 == 1)
                {
                    positions.push_back(i + 1);
                    k--;
                }

                i++;
            }

            positions.push_back(n);
        }

        if (ans)
        {
            cout << "YES" << endl;
            for (auto val : positions)
                cout << val << " ";

            cout << endl;
        }

        else
            cout << "NO" << endl;
    }

    return 0;
}
