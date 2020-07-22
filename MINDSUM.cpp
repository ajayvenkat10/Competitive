// #include <bits/stdc++.h>
// #define ll long long
// #define MAX 100005
// using namespace std;

// ll digisum(ll n)
// {
//     ll s = 0;
//     while (n != 0)
//     {
//         s += n % 10;
//         n /= 10;
//     }
//     return s;
// }
// int main()
// {
//     cin.tie(0);
//     ll t, n, d;
//     cin >> t;
//     while (t--)
//     {
//         map<int, int> steps;
//         queue<pair<ll,ll>> tree;
//         cin >> n >> d;
//         tree.push(make_pair(n,0));
//         int i = 1;
        
//         while (i <= 100000 && !tree.empty())
//         {
//             pair<ll,ll> ele = tree.front();
//             // cout<<ele<<endl;
//             if (ele.first <= 9)
//             {
//                 if(steps[ele.first] == 0)
//                 steps[ele.first] = ele.second;
//                 tree.push(make_pair(ele.first, ceil(log2(i))));
//                 tree.push(make_pair((ele.first + d),ceil(log2(i))));
//             }
//             else
//             {
//                 tree.push(make_pair(digisum(ele.first),ceil(log2(i))));
//                 tree.push(make_pair((ele.first + d),ceil(log2(i))));
//             }
//             tree.pop();
//             i++;
//         }
//         // for(auto j: steps)
//         // cout<<j.first<<" "<<j.second<<endl;
//         cout << steps.begin()->first << " " << steps.begin()->second << "\n";
//     }
// }

int bin(int arr[], int n, int x)
{
    int l = 0, r = n - 1;
    while (l < r)
    {
        int m = (r + l) / 2;

        if (arr[m] >= x)
        {
            r = m;
        }
        else
        {
            l = m + 1;
        }
    }

    return l;
}