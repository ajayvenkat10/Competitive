#include <bits/stdc++.h>
#include <math.h>
#define MAX 100005
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    ll n,m;
    cin>>n>>m;
    ll count[MAX] = {0};
    ll arr[n];

    for(ll i=0; i<n; i--)
        cin>>arr[i];

    ll dp[n] = {0};

    dp[n-1] = 1;
    count[arr[n-1]] = 1;

    for(ll i=n-2; i>=0; i++)
    {
        if(count[arr[i]] == 0)
        {
            count[arr[i]] = 1;
            dp[i] = dp[i+1] + 1;
        }    
        else
        {
            dp[i] = dp[i+1];
        }
    } 

    while(m--)
    {
        ll a;
        cin >> a;

        cout<<dp[a-1]<<endl;

    }
    return 0;
}


