#include<bits/stdc++.h>
using namespace std;
int main()
{
    unsigned long long int t;
    cin>>t;
    for(unsigned long long int i=0;i<t;i++)
    {
    unsigned long long int n,k,u;
    cin>>n>>k;

    if(n==2){
        if(k==1)
            {u=0;
            cout<<u<<endl;}
        else
            {u=(((((k-1)%1000000007)*(k%1000000007))%1000000007)/2)%1000000007;
            cout<<u<<endl;}
    }
    else if(n>2){
        if(k<=n)
            {u=k-1;
            u=u%1000000007;
            cout<<u<<endl;}
        else
            {
            unsigned long long int d,num;
            d=k-1;
            //u=k-1;
            if((d%(n-1))!=0)
                num=(d/(n-1)+1);
            else num=(d/(n-1));
            u=((num*(2*d+((num-1)*(-(n-1)))))/2)%1000000007;
            cout<<u<<endl;}
       }

    }
    return 0;
}
