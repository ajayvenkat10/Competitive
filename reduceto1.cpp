#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000000007
#define ll long long
using namespace std;
ll fact_arr[1000003];

void calculate()
{   fact_arr[0] = 1;
    for(ll i = 1; i<=1000007; i++)
    {
        fact_arr[i] = (i*fact_arr[i-1])%MAX;
    }
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    calculate();

    ll t;
    cin >> t;
    while(t--)
    {   ll n,ans=0;
        cin>>n;
        ans = fact_arr[n+1] - 1;
        cout<<ans<<endl;
    }
    return(0);
}
