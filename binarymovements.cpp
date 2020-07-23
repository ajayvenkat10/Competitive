#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000000
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    ll t;
    cin>> t;
    while(t--)
    {
        ll n,z;
        cin>>n>>z;

        ll arr1[1000000];
        ll arr2[1000000];


        for(ll i = 0; i<n; i++)
        {
            cin>>arr1[i];
            arr2[i] = arr1[i];
        }

        for(ll i=0;i<z;i++)
        {
            for(ll j=0;j<n-1;j++)
            {
                if(arr1[j]==0 && arr1[j+1]==1)
                {
                    arr2[j] = 1;
                    arr2[j+1] = 0;
                }
            }

            for(ll k=0;k<n;k++)
                arr1[k] = arr2[k];
        }

        for(ll i=0;i<n;i++)
            cout<<arr1[i]<<" ";

        cout<<endl;
    }
    return 0;
}
