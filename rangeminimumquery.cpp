#include<bits/stc++.h>
#define ll long long 
using namespace std;

ll getMid(ll s,ll e)
{
    return((s+e/2));
}

int main() 
{ 
    ll n,q;
    cin>>n;
    ll arr[100005];
    
    for(ll i=0; i<n; i++)
        cin>>arr[i];
    
    ll *st = constructST(arr, n); 

    cin>>q;

    while(q--)
    {   
        ll start,end;
        cin>>start>>end;

        cout<<RMQ(st, n, start, end)<<endl;
    }
	return 0; 
} 