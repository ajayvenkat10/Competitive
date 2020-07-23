#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000000
#define ll long long
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    ll t;
    cin>> t;
    while(t--)
    {   ll r,c,i,j,k,count,adj_count;
        cin>>r>>c;
        ll arr[10][10];

        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                cin>>arr[i][j];
            }
        }
        count = 0;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {   adj_count = 0;
                ll poss_arr[4] = {0};
                poss_arr[0] = i-1;
                poss_arr[1] = j-1;
                poss_arr[2] = i+1;
                poss_arr[3] = j+1;

                for(k=0;k<4;k++)
                {   if(k%2==0)
                    {
                        if(poss_arr[k]>=0 && poss_arr[k]<r)
                            adj_count++;
                    }

                    else
                    {
                        if(poss_arr[k]>=0 && poss_arr[k]<c)
                            adj_count++;
                    }
                }

                if(arr[i][j]<adj_count)
                    count++;
            }
        }
    
        if(count == r*c)
            cout<<"Stable"<<endl;

        else
            cout<<"Unstable"<<endl;
    }
    return 0;
}
