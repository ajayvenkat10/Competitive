#include<bits/stdc++.h>
using namespace std;

int main(){

    int n,k;
    int arr[30005]={0};
    cin>>n>>k;

    for(int i=1; i<n; i++)
        cin>>arr[i];

    int pointer = 1;

    while(pointer < k){
        pointer += arr[pointer];
        if(pointer == k){
            cout<<"YES"<<endl;
            return 0;
        }
    }

    cout<<"NO"<<endl;
    return 0;
}