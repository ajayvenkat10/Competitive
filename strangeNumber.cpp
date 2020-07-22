#include<bits/stdc++.h>
#include<cmath>
#define ll long long
using namespace std;

ll count_of_prime_factors = 0;
void primeFactors(ll n) 
{ 
	while (n % 2 == 0) 
	{  
        count_of_prime_factors++;
		n = n/2; 
	} 

	for (ll i = 3; i <= sqrt(n); i = i + 2) 
	{ 
		while (n % i == 0) 
		{ 
			count_of_prime_factors++;
			n = n/i; 
		} 
	} 

	if (n > 2) 
		count_of_prime_factors++; 
} 

int main(){

    ll t;
    cin >> t;

    while(t--){

        ll n,k;

        cin >> n >> k;

        count_of_prime_factors = 0;

        primeFactors(n);
        
        if(count_of_prime_factors >= k)
            cout<<1<<endl;

        else
            cout<<0<<endl;
    }

    return 0;
}