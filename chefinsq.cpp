#include <bits/stdc++.h>

using namespace std;
long long int fact(int d, int f)
{
    long long int res, i;
    res = 1;
    for (i = d + 1; i <= f; i++)
    {
        res = res * i;
    }
    return res;
}

int main()
{
    int t;
    int k, n, i, j, ldi, lfreq;

    long long int sum = 0;
    long long int ncr, d, max, min, temp;

    cin >> t;
    while (t--)
    {

        cin >> n >> k;
        int a[n] = {0};
        int b[101] = {0};
        int c[101] = {0};
        int r = 0;

        for (i = 0; i < n; i++)
        {
            cin >> a[i];
            j = a[i];
            b[j]++;
        }
        sort(a, a + n);
        ldi = a[k - 1];
        lfreq = b[ldi];
        for (i = 0; i < k; i++)
        {
            if (a[i] == ldi)
            {
                r++;
            }
        }
        d = lfreq - r;

        if (d > r)
        {
            max = d + 1;
            min = r;
        }
        else
        {
            max = r + 1;
            min = d;
        }
        i = 0;
        while (max <= lfreq)
        {
            c[i] = max;
            max++;
            i++;
        }
        temp = i;
        for (j = 2; j <= min; j++)
        {
            for (i = 0; i < temp; i++)
            {
                if (c[i] % j == 0)
                {
                    c[i] = c[i] / j;
                    break;
                }
            }
        }

        ncr = 1;
        for (i = 0; i < temp; i++)
        {
            ncr = c[i] * ncr;
        }
        cout << ncr << endl;
    }
}