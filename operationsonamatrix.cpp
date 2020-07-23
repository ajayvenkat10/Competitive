#include <bits/stdc++.h>
#define ll long long
#define MAX 100005
using namespace std;

int main()
{
    ll t;
    cin >> t;

    while (t--)
    {
        ll N, M, Q;
        cin >> N >> M >> Q;
        ll rows[N] = {0};
        ll cols[M] = {0};

        while (Q--)
        {
            ll r, c;
            cin >> r >> c;
            r -= 1;
            c -= 1;

            rows[r]++;
            cols[c]++;
        }

        ll e = 0, o = 0;

        for (ll i = 0; i < M; i++)
        {
            if (cols[i] % 2 == 1)
                o++;

            else
                e++;
        }

        ll odd_count = 0;

        for (ll i = 0; i < N; i++)
        {
            if (rows[i] % 2 == 1)
                odd_count = odd_count + e;

            else
                odd_count = odd_count + o;
        }

        cout << odd_count << endl;
    }
    return 0;
}