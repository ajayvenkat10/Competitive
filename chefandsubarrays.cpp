#include<bits/stdc++.h>
#define ll long long 
#define MAX 100005
using namespace std;

ll segtree[4 * MAX];

void construct_segtree(ll array[], ll node, ll start, ll end)
{
    if(start == end)
    {
        segtree[node] = array[start];
        return;
    }   
    
    ll mid = (start + end)/2;
    construct_segtree(array, (2*node)+1, start, mid);
    construct_segtree(array, (2*node)+2, mid + 1, end);

    segtree[node] = segtree[(2*node)+1] | segtree[(2*node)+2];
}

ll or_of_range(ll node, ll start, ll end, ll L, ll R)
{
    if(start > end || start > R || end < L)
        return 0;

    if(start >= L && end <= R)
        return segtree[node];

    ll mid = (start + end)/2;
    ll range1 = or_of_range(2*node+1,start,mid,L,R);
    ll range2 = or_of_range(2*node+2,mid+1,end,L,R);

    return (range1 | range2);
}

int main()
{
    ll t;
    cin >> t;

    while(t--)
    {   
        ll n,k;
        ll arr[MAX];
        cin>>n>>k;

        for(ll i=0; i<n; i++)
            cin>>arr[i];

        construct_segtree(arr,0,0,n-1);

        ll count = 0;
        for(ll i=0; i<n; i++)
        {
            ll low = 0;
            ll high = n-1;

            ll pos = n;

            while(low <= high)
            {
                ll mid = (low+high)/2;

                if(or_of_range(0,0,n-1,i,mid) >= k)
                {
                    pos = min(pos,mid);
                    high = mid - 1;
                }
                else
                    low = mid + 1;
            }
            
            count += (n - pos);
        }
        
        cout << count << endl;
    }
    return 0;
}