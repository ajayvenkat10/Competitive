// ll getMid(ll s, ll e) {
// 	return s + (e - s)/2;
// }
//
// ll getXorUtil(ll *st, ll ss, ll se, ll qs,
// 			ll qe, ll si)
// {
// 	if (qs <= ss && qe >= se)
// 		return st[si];
//
// 	if (se < qs || ss > qe)
// 		return 0;
//
// 	ll mid = getMid(ss, se);
// 	return getXorUtil(st, ss, mid, qs, qe, 2*si+1) ^
// 		getXorUtil(st, mid+1, se, qs, qe, 2*si+2);
// }
//
// ll getXor(ll *st, ll n, ll qs, ll qe)
// {
// 	if (qs < 0 || qe > n-1 || qs > qe)
// 	{
// 		printf("Invalid Input");
// 		return 0;
// 	}
//
// 	return getXorUtil(st, 0, n-1, qs, qe, 0);
// }
//
// ll constructSTUtil(ll arr[], ll ss, ll se,
// 					ll *st, ll si)
// {
//
// 	if (ss == se)
// 	{
// 		st[si] = arr[ss];
// 		return arr[ss];
// 	}
// 	ll mid = getMid(ss, se);
// 	st[si] = constructSTUtil(arr, ss, mid, st, si*2+1) ^
// 			constructSTUtil(arr, mid+1, se, st, si*2+2);
// 	return st[si];
// }
//
// ll *constructST(ll arr[], ll n)
// {
// 	ll x = (ll)(ceil(log2(n)));
//
// 	ll max_size = 2*(ll)pow(2, x) - 1;
//
// 	ll *st = new ll[max_size];
//
// 	constructSTUtil(arr, 0, n-1, st, 0);
//
// 	return st;
// }
//
// int main()
// {
//     ll t;
//     cin >> t;
//
//     while(t--)
//     {
//     	ll arr[1000005];
//         ll n;
//         cin >> n;
//
//         for(ll i = 0; i<n; i++)
//             cin >> arr[i];
//
//     	ll *st = constructST(arr, n);
//         ll count = 0;
//
//         for(ll i=0; i<n; i++)
//         {
//             for(ll j=i+1; j<n; j++)
//             {
//                 for(ll k=j; k<n; k++)
//                 {
//                     if(getXor(st,n,i,j-1) == getXor(st,n,j,k))
//                         count += 1;
//                 }
//             }
//         }
//
//         cout<<count<<endl;
//     }
//     return 0;
// }
// #include <bits/stdc++.h>
// #include <math.h>
// using namespace std;
// #define ll long long
//
// int main()
// {
// 	vector<int> a = {3,6,13,8,15};
// 	unordered_map<int, int> hashMap;
// 	int number_of_elements = a.size();
// 	hashMap[0] = -1;
// 	int xor_sum = 0;
// 	for(int i = 0; i < number_of_elements; i++) {
// 	    xor_sum ^= a[i];
// 	    if(hashMap.find(xorSum) != hashMap.end()) {
// 	        cout << hashMap[xorSum] + 1 << " " << i << endl;
// 	        break;
// 	    }
// 	    hashMap[xor_sum] = i;
// 	}
// 	return 0;
// }

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector< pair<int, int> > findSubArrays(int arr[], int n)
{
	unordered_map<int, vector<int> > map;
 	vector <pair<int, int>> out;

	int sum = 0;

	for (int i = 0; i < n; i++)
	{
		// add current element to sum
		sum ^= arr[i];

		// if sum is 0, we found a subarray starting
		// from index 0 and ending at index i
		if (sum == 0)
			out.push_back(make_pair(0, i));

		// If sum already exists in the map there exists
		// at-least one subarray ending at index i with
		// 0 sum
		if (map.find(sum) != map.end())
		{
			// map[sum] stores starting index of all subarrays
			vector<int> vc = map[sum];
			for (auto it = vc.begin(); it != vc.end(); it++)
				out.push_back(make_pair(*it + 1, i));
		}

		// Important - no else
		map[sum].push_back(i);
	}

	// return output vector
	return out;
}

// Utility function to print all subarrays with sum 0
void print(vector<pair<int, int>> out)
{
	for (auto it = out.begin(); it != out.end(); it++)
		cout << "Subarray found from Index " <<
			it->first << " to " << it->second << endl;
}

// Driver code
int main()
{
	int arr[] = {5,2,7,2,4,6};
	int n = sizeof(arr)/sizeof(arr[0]);

	vector<pair<int, int> > out = findSubArrays(arr, n);

	// if we didn’t find any subarray with 0 sum,
	// then subarray doesn’t exists
	if (out.size() == 0)
		cout << "No subarray exists";
	else
		print(out);

	return 0;
}
