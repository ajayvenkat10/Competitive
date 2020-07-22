#include <bits/stdc++.h>
#define ll long long
#define MAX 200005
using namespace std;

int main()
{
    ll t;
    cin >> t;

    while (t--)
    {
        ll n, k;
        cin >> n >> k;

        ll arr[MAX] = {0};
        vector<ll> maximum;
        vector<ll> minimum;
        map<ll, ll> sum_count;

        for (ll i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        for (ll i = 0; i < n / 2; i++)
        {
            maximum.push_back(max(arr[i], arr[n - 1 - i]));
            minimum.push_back(min(arr[i], arr[n - 1 - i]));

            sum_count[arr[i] + arr[n - 1 - i]]++;
        }

        sort(maximum.begin(), maximum.end());
        sort(minimum.begin(), minimum.end());

        ll ans = n / 2; //Answer is atmost n/2 always.

        for (auto distinct : sum_count)
        {
            ll bs_ans;
            ll sum = distinct.first;
            ll count = distinct.second;

            ll low = 0;
            ll high = n / 2 - 1;

            //Binary search on maximum array when sum is greater than k
            //to find the position of the first element whose difference result with
            //the sum value is between 1 to k (inclusive)

            if (sum > k)
            {
                while (low < high)
                {
                    ll mid = (low + high) / 2;
                    if (sum - maximum[mid] <= k)
                        high = mid;
                    else
                        low = mid + 1;
                }
                bs_ans = (n / 2 - low) - count + (low * 2);
            }

            //Binary search on minimum array when sum is less than  or equal to k
            //to find the position of the first element greater than or equal to th sum value

            else
            {
                while (low < high)
                {
                    ll mid = (low + high) / 2;
                    if (minimum[mid] < sum)
                        low = mid + 1;
                    else
                        high = mid;
                }

                //Corner for my implementation:
                //Low pointer will end up at the last index in the array if there is no such element
                //greater than or equal to the sum value

                if (minimum[low] < sum)
                    low++;

                bs_ans = low - count + ((n / 2 - low) * 2);
            }

            ans = min(ans, bs_ans);
        }

        cout << ans << endl;
    }
}