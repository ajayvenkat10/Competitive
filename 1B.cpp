#include<bits/stdc++.h>
#include <math.h>
#define MAX 2005
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 8;
	int count = 0;

	for(int i=n; i>0; i/=2)
	{
		for(int j=0; j<i; j++)
			count += 1;
	}
	// x = x/2;
	// int i = 0;
	// for(i = 1; x>0; x = x/2)
	// 	i += 1;

	cout<<count;

	
	// int t;
	// cin>>t;
	// int T = t;
	// while(t--)
	// {   int P,Q,x,y;
	// 	char d;
	// 	int ans_x = 0, val_x = 0;
	// 	int ans_y = 0, val_y = 0;
    //     cin>> P >> Q;

	// 	int X[Q+1] = {0};
	// 	int Y[Q+1] = {0};

	// 	while(P--)
	// 	{
	// 		cin>> x >> y >> d;
	// 		if(d == 'N')
	// 		{
	// 			for(int i=y+1; i<=Q; i++)
	// 				Y[i]++;
	// 		}
	// 		else if(d == 'S')
	// 		{
	// 			for(int i=0; i<y; i++)
	// 				Y[i]++;
	// 		}
	// 		if(d == 'E')
	// 		{
	// 			for(int i=x+1; i<=Q; i++)
	// 				X[i]++;
	// 		}
	// 		if(d == 'W')
	// 		{
	// 			for(int i=0; i<x; i++)
	// 				X[i]++;
	// 		}
	// 	}

	// 	for(int i=0; i<=Q; i++)
	// 	{
	// 		if(X[i] > val_x)
	// 		{	val_x = X[i];
	// 			ans_x = i;
	// 		}

	// 		if(Y[i] > val_y)
	// 		{
	// 			val_y = Y[i];
	// 			ans_y = i;
	// 		}
	// 	}

	// 	cout<<"Case #"<<T-t<<": "<<ans_x<<" "<<ans_y<<endl;
    // }

	return(0);
}
