#include<iostream>
#define ll long long
using namespace std;

//function to find factorial of given number
unsigned int factorial(unsigned int n)
{
    if (n == 0)
    return 1;
    return n * factorial(n - 1);
}

// ll factorial(ll n)
// {
//     if (n == 0)
//     return 1;
//     return n * factorial(n - 1);
// }

// Driver code
int main()
{
    int num = 25;
    cout << "Factorial of " << num << " is " << (factorial(num+1) - 1)%1000000007 << endl;
    return 0;
}
