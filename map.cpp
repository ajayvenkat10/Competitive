#include<bits/stdc++.h>
using namespace std;

int main(){

    map<int, int> sample_map;
    map<int, int> sample_map_dup;


    sample_map[1] = 2;
    sample_map[2] = 3;
    // sample_map.insert({1,2});
    // sample_map.insert({2,3});
    // sample_map.insert({3,4});
    // sample_map.insert({4,5});

    // sample_map_dup.insert({1,3});
    // sample_map_dup.insert({2,4});
    // sample_map_dup.insert({5,6});
    // sample_map_dup.insert({7,8});

    // for(auto it : sample_map){
    //     sample_map[it.first] += sample_map_dup[it.first];
    // }

    // cout<<"Pass 1"<<endl;
    // for(auto it : sample_map){
    //     cout<<sample_map[it.first]<<endl;
    // }

    // sample_map.insert(sample_map_dup.begin(),sample_map_dup.end());

    // cout<<"Pass 2"<<endl;

    for(auto it : sample_map){
        cout<<it.first<<" "<<it.second<<endl;
    }

    return 0;
}