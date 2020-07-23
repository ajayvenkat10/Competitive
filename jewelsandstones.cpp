#include <bits/stdc++.h>
#include <math.h>
#include <cmath>
#define ll long long 
using namespace std;

int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n,k,an=0,d=0;
		ll num = 0, sum = 0, a0=0;
        cin>>n>>k;
        an=k-1;
        if(n>=k)
               sum=an % 1000000007;
        else
        {
			d=n-1;
            if(n==2)
                sum=(an*(an+1))/2;
            else
            {
                num=(an/d + 1);
                a0= an-((num-1)*d);
                sum=((num*(a0+an))/2) % 1000000007;
            }
        }
        cout<<sum % 1000000007<<endl;
    }
    return 0;
}
