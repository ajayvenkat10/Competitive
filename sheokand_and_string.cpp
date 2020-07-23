#include <bits/stdc++.h>
#include <math.h>
#define MAX 1000005
#define ll long long
using namespace std;

int pointer,n,q;
string strings_arr[MAX],answer[MAX];

struct node
{
    int count;
    bool finish;
    int child[26];

} trie[MAX];

void addWord(string word)
{
    int root = 0;
    for(auto &ch : word)
    {
        if(!trie[root].child[ch - 'a'])
        {
            pointer ++;
            trie[root].child[ch - 'a'] = pointer;
        }

        root = trie[root].child[ch - 'a'];
    }
    trie[root].finish = true;
}

string getLongestCommonPrefix(string word)
{
    string ans;
    int root = 0;
    for(auto &ch : word)
    {
        if(!trie[root].child[ch - 'a'])
            break;

        ans += ch;
        root = trie[root].child[ch - 'a'];
    }

    while(!trie[root].finish)
    {
        for(int i=0; i<26; i++)
        {
            if(trie[root].child[i])
            {
                root = trie[root].child[i];
                ans += (char)(i + 'a');
                break;
            }
        }
    }

    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    vector <pair <ll, string> > tuple[MAX];
    cin>>n;
    for(ll i=0; i<n; i++)
        cin>>strings_arr[i];

    cin>>q;
    for(ll i=0; i<q; i++)
    {
        ll length;
        string word;

        cin>>length>>word;

        tuple[length-1].push_back(make_pair(i,word));
    }

    for(ll i=0; i<n; i++)
    {
        addWord(strings_arr[i]);

        for(auto &queries : tuple[i])
            answer[queries.first] = getLongestCommonPrefix(queries.second);
    }

    for(ll i=0; i<q; i++)
        cout<<answer[i]<<endl;

    return 0;
}
