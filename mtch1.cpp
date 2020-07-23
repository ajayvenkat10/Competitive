#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000000007
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    ll t;
    cin>> t;
    while(t--)
    {
        ll pile1, pile2;
        ll quotient,reaminder;
        cin>>pile1>>pile2;

        ll count = 0;
        while(1)
        {
            if(pile1 == pile2)
            {
                count++;
                break;
            }
            else
            {
                if(pile1>pile2)
                {
                    if(pile1/pile2 > 1)
                    {
                        count++;
                        break;
                    }
                    pile1=pile1-pile2;
                }

                else
                {
                    if(pile2/pile1 > 1)
                    {
                        count++;
                        break;
                    }
                    pile2 = pile2 - pile1;
                }
                count++;
            }
        }

        if(count%2 == 0)
            cout<<"Rich"<<endl;
        else
            cout<<"Ari"<<endl;
    }
    return 0;
}
