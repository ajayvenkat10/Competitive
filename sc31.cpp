#include<iostream>
using namespace std;
int main()
{
	int t,n;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		int count=0;
		long long int num1, num2, final2;
		for(int j=0;j<n;j++)
		{
			if(j==0){
			cin>>num1;
			}
			else if(j>=1)
			{
				cin>>num2;
				num1 = num1^num2;
			}
		}
		// for(int j=0;j<n-1;j++)
		// {
		// 	final = arr[j]^arr[j+1];
		// }
		final2 = num1;
		for(int j=0;j<10;final2/=10)
		{
			if((final2%10)==1)
				count++;
		}
		cout<<count<<endl;

	}

	return 0;
}