#include <bits/stdc++.h>
using namespace std;
int calc(int n)
{
    int ans = 0;
    if (n == 0)
        return 0;
    else
    {
        while (n != 1)
        {
            ans += n % 2;
            n = n / 2;
        }
        ans += 1;
    }
    return ans;
}
int fun(int arr[], int x, int k, int n)
{
    int val = 0;
    for (int i = 1; i <= x; i++)
    {
        val += arr[i];
    }
    if (val >= k)
        return true;
    for (int i = x + 1; i <= n; i++)
    {
        val -= arr[i - x];
        val += arr[i];
        if (val >= k)
            return true;
    }
    return false;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, q;
    cin >> n >> q;
    int arr[100001];
    arr[0] = 0;
    for (int i = 1; i <= n; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = calc(temp);
    }
    while (q--)
    {
        int k;
        cin >> k;
        int ans = INT_MAX;
        int l = 1, r = n;
        while (l <= r)
        {
            int mid = l + ((r - l) / 2);
            if (fun(arr, mid, k, n))
            {
                ans = min(ans, mid);
                r = mid - 1;
            }
            else
                l = mid + 1;
        }
        if (ans == INT_MAX)
            cout << -1 << "\n";
        else
            cout << ans << "\n";
    }
}