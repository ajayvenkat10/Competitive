#include <bits/stdc++.h>
#include <cstdlib>
#include <math.h>
#include <cmath>
#include <string>

#define MAX 1000005
#define ll long long
using namespace std;

bool isPrime(ll num)
{
    if(num < 2)
        return(false);

    for(ll i=2; i<sqrt(num)+1; i++)
    {
        if(num%i == 0)
            return(false);
    }
    return(true);

}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    int primes1[1000], primes2[1000];
    int n1,n2;
    int ans;
    cin>>n1>>n2;
    int pos = 0;
    int k = 0;
    for(int i=n1; i<=n2; i++)
    {
        if(isPrime(i))
            primes1[pos++] = i;
    }

    if(pos == 0)
        ans = 0;

    else
    {
        for(int i=0; i<pos; i++)
        {
            for(int j=0; j<pos; j++)
            {
                if(i!=j)
                {
                    string a = to_string(primes1[i]);
                    string b = to_string(primes1[j]);
                    a = a+b;
                    int number = stoi((a));
                    cout<<number<<endl;
                    if(isPrime(number))
                        primes2[k++] = number;
                }
            }
        }

        std::set<int>s(begin(primes2), end(primes2));

        if(s.size() == 0)
            ans = 0;
        else
        {
            ll x = *s.begin();
            ll y = *s.rbegin();
            ll z = 0;
            for(ll i=2; i<s.size(); i++)
            {
                z = x+y;
                x = y;
                y = z;
            }
            ans = z;
        }
    }

    cout<<ans<<endl;

    return 0;

}
