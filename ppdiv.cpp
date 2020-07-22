// CPP Program to count the numbers 
// within a range such that number 
// can be expressed as power of some 
// other number 
#include <bits/stdc++.h> 
#define ll long long

using namespace std; 

#define N 1000005 
#define MAX 1e18 

// Vector to store powers greater than 3 
vector<ll> powers; 

// set to store perfect squares 
set<ll> squares; 

// set to store powers other 
// than perfect squares 
set<ll> s; 

void powersPrecomputation() 
{ 
	for (ll i = 2; i < N; i++) 
	{ 
		// pushing squares 
		squares.insert(i * i); 

		// if the values is already 
		// a perfect square means 
		// present in the set 
		if (squares.find(i) != squares.end()) 
				continue; 

		ll temp = i; 

		// run loop until some 
		// power of current number 
		// doesn't exceed MAX 
		while (i * i <= MAX / temp) 
		{ 
			temp *= (i * i); 

			/* pushing only odd powers 
			as even power of a number 
			can always be expressed as 
			a perfect square which is 
			already present in set squares */
			s.insert(temp); 
		} 
	} 

	// Inserting those sorted 
	// values of set into a vector 
	for (auto x : s) 
		powers.push_back(x); 
} 

ll calculateAnswer(ll L, ll R) 
{ 
	// calculate perfect squares in 
	// range using sqrtl function 
	ll perfectSquares = floor(sqrtl(R)) - 
							floor(sqrtl(L - 1)); 

	// calculate upper value of R 
	// in vector using binary search 
	ll high = (upper_bound(powers.begin(), 
			powers.end(), R) - powers.begin()); 

	// calculate lower value of L 
	// in vector using binary search 
	ll low = (lower_bound(powers.begin(), 
			powers.end(), L) - powers.begin()); 

	// add into final answer 
	perfectSquares += (high - low); 

	return perfectSquares; 
} 

// Driver Code 
int main() 
{ 
	// precompute the powers 
	powersPrecomputation(); 

	// left value of range 
	ll L = 12; 
	
	// right value of range 
	ll R = 29; 

	cout << "Number of powers between " << L 
			<< " and " << R << " = " << 
			calculateAnswer(L, R) << endl; 

	L = 1; 
	R = MAX; 

	cout << "Number of powers between " << L 
			<< " and " << R << " = " << 
			calculateAnswer(L, R) << endl; 

	return 0; 
} 
