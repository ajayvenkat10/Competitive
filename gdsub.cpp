#include <bits/stdc++.h>
#define ll long long
#define MOD 1000000007
using namespace std;

const ll MAX = 100005;
const ll MAX_PRIMES = 1010;
const ll MAX_RANGE = 8010;

int main()
{
    ll n, k;
    ll frequency[MAX_RANGE] = {0};
    ll sequence_of_primes[MAX] = {0};

    cin >> n >> k;

    for (ll i = 0; i < n; i++)
    {
        cin >> sequence_of_primes[i];
        frequency[sequence_of_primes[i]]++;
    }

    vector<ll> occured_primes;
    occured_primes.push_back(0);

    for (ll i = 0; i < MAX_RANGE; i++)
    {
        if (frequency[i] > 0)
            occured_primes.push_back(frequency[i]);
    }

    k = min(k, (ll)occured_primes.size() - 1);

    ll dp[MAX_PRIMES][MAX_PRIMES];
    memset(dp, 0, sizeof(dp));

    dp[0][0] = 1;

    for (ll i = 1; i < occured_primes.size(); i++)
    {
        dp[i][0] = 1;

        for (ll j = 1; j <= k; j++)
        {
            dp[i][j] = (dp[i - 1][j] + (dp[i - 1][j - 1] * occured_primes[i]) % MOD) % MOD;
        }
    }

    ll distinct_primes = occured_primes.size() - 1;

    ll valid_subsequences = 0;

    for (ll i = 0; i <= k; i++)
    {
        valid_subsequences = (valid_subsequences + dp[distinct_primes][i]) % MOD;
    }

    cout << valid_subsequences << endl;

    return 0;
}