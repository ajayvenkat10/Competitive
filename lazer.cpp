#include <bits/stdc++.h>
#define ll long long
#define  MAX 100005  
using namespace std;

ll N, sweep_line[MAX]={0};

struct segment{
    ll y_coordinate,position,type;
    bool operator<(const segment &s ) const{
        return make_pair(y_coordinate,type) < make_pair(s.y_coordinate,s.type);
    }
};

void update(ll position, ll value){
    for (ll i = position+1; i < N; i+= i & -i)
        sweep_line[i] += value; 
}

ll query(ll position){
    ll range_sum = 0;

    for(ll i = position; i; i-= i & -i){
        range_sum += sweep_line[i];
    }

    return range_sum;
}

int main() {

    ll t;
    cin>>t;

    while(t--){
        ll Q, A[MAX], count[MAX], x1[MAX], x2[MAX], y[MAX];

        cin >> N >> Q;

        for (ll i = 0; i < N; i++)
            cin >> A[i];

        for (ll i = 0; i < Q; i++)
        {
            cin >> x1[i] >> x2[i] >> y[i];
            x1[i]--;
            x2[i]--;
        }

        vector<segment> vector_all;

        for (ll i = 0; i < N-1; i++)
        {
            vector_all.push_back({min(A[i], A[i+1]), i, 1});
            vector_all.push_back({max(A[i], A[i+1]), i, 3});
        }
        
        for (ll i = 0; i < Q; i++)
            vector_all.push_back({y[i], i, 2});

        sort(vector_all.begin(), vector_all.end());
        
        for (auto &seg : vector_all)
        {
            if(seg.type == 1)
                update(seg.position, 1);

            else if(seg.type == 2)
                count[seg.position] = query(x2[seg.position]) - query(x1[seg.position]);   

            else
                update(seg.position, -1);
        }
        
        for (ll i = 0; i < Q; i++)
            cout<<count[i]<<endl;
        
    }
    return 0;
}
