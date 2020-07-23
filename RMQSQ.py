#include <bits/stdc++.h> 
#define ll long long 
using namespace std; 

ll minVal(ll x, ll y) { return (x < y)? x: y; } 
 
ll getMid(ll s, ll e) { return s + (e -s)/2; } 

ll RMQUtil(ll *st, ll ss, ll se, ll qs, ll qe, ll index) 
{ 
	if (qs <= ss && qe >= se) 
		return st[index]; 

	if (se < qs || ss > qe) 
		return INT_MAX; 

	ll mid = getMid(ss, se); 
	return minVal(RMQUtil(st, ss, mid, qs, qe, 2*index+1), 
				RMQUtil(st, mid+1, se, qs, qe, 2*index+2)); 
} 

ll RMQ(ll *st, ll n, ll qs, ll qe) 
{ 
	if (qs < 0 || qe > n-1 || qs > qe) 
	{ 
		cout<<"Invalid Input"; 
		return -1; 
	} 

	return RMQUtil(st, 0, n-1, qs, qe, 0); 
} 

ll constructSTUtil(ll arr[], ll ss, ll se, 
								ll *st, ll si) 
{ 
	if (ss == se) 
	{ 
		st[si] = arr[ss]; 
		return arr[ss]; 
	} 

	ll mid = getMid(ss, se); 
	st[si] = minVal(constructSTUtil(arr, ss, mid, st, si*2+1), 
					constructSTUtil(arr, mid+1, se, st, si*2+2)); 
	return st[si]; 
} 

ll *constructST(ll arr[], ll n) 
{ 

	ll x = (ll)(ceil(log2(n))); 

	ll max_size = 2*(ll)pow(2, x) - 1; 

	ll *st = new ll[max_size]; 

	constructSTUtil(arr, 0, n-1, st, 0); 

	return st; 
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

