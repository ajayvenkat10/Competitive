#include <iostream>
const long m = 1000000007;
using namespace std;

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long int k;
        long int n;
        cin >> n >> k;
        long int a = k - n;
        long int sum = 0;
        if (a > 0)
        {
            if (n == 2)
                sum = ((((k % m) * ((k - 1) % m)) % m) / 2) % m;

            else
            {
                long int d = (1 - n) % m;
                long int num = ((d - a) / d) % m;
                long int l = ((a + (num - 1)) % m * d) % m;
                sum = (((((a + l) % m) * (num % m)) % m) / 2) % m;
                sum = (sum + (k - 1) % m) % m;
            }
        }

        else
        {
            sum = (k - 1) % m;
        }

        cout << sum << endl;
    }
    return 0;
}
