// #include <bits/stdc++.h>
// #include <math.h>
// #define MAX 1000000
// #define ll long long
// using namespace std;
//
// ll dp[2507][2507];
// ll arr[2507];
// ll location[1000007];
// // ll n;
// ll max_length(ll i, ll j)
// {
//     // if (i < 0 || j < 0 || i >= n || j >= n)
// 	// 	return 0;
//
//     if(i==0)
//     {
//         dp[i][j] = 2;
//         return(dp[i][j]);
//     }
//
//     else if(dp[i][j] != 0)
//     {
//         return(dp[i][j]);
//     }
//
//     else
//     {
//         ll diff = arr[j]-arr[i];
//         ll previousEle = arr[i] - diff;
//         if(previousEle < 0)
//         {
//             dp[i][j] = 2;
//             return dp[i][j];
//         }
//         else
//         {
//             ll previousIndex = location[previousEle];
//             if(previousIndex == -1)
//             {
//                 dp[i][j] = 2;
//                 return(dp[i][j]);
//             }
//
//             else
//             {
//                 return dp[i][j] = max_length(previousIndex,i) + 1;
//             }
//         }
//     }
// }
//
// int main()
// {
//     ios_base::sync_with_stdio(false);
// 	cin.tie(NULL);
//     ll n;
//     memset(dp,0,sizeof(dp));
//     memset(location,-1,sizeof(location));
//     cin>>n;
//     for(ll i=0; i<n; i++)
//         cin>>arr[i];
//
//     sort(arr,arr+n);
//     for(ll i=0; i<n; i++)
//         location[arr[i]] = i;
//
//     ll maxi = 0;
//     for(ll i=0;i<n;i++)
//     {
//         for(ll j=0;j<n;j++)
//         {   if(i!=j)
//             {
//                 maxi = max(maxi,max_length(i,j));
//             }
//         }
//     }
//
//     cout<<maxi<<endl;
//
//     return 0;
// }

#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000000
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    ll n;
    ll dp[100007][100007]={0};
    ll arr[2503];
    ll diff;
    cin>>n;
    for(ll i=0; i<n; i++)
        cin>>arr[i];

    sort(arr,arr+n);

    ll max = 0;
    for(ll i=0;i<n-1;i++)
    {
        for(ll j=i+1;j<n;j++)
        {   diff = arr[j]-arr[i];
            if(i==0)
                dp[arr[j]][diff] = 2;

            else
            {
                if(dp[arr[i]][diff] == 0)
                    dp[arr[j]][diff] = 2;

                else
                    dp[arr[j]][diff] = dp[arr[i]][diff] + 1;
            }

            if(dp[arr[j]][diff] > max)
                max = dp[arr[j]][diff];
        }
    }

    cout<<max<<endl;

    return 0;
}
