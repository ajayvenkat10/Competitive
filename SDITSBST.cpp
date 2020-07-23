#include <bits/stdc++.h>
#define ll long long
#define MAX 100005
using namespace std;

ll arr[MAX];
ll ind = 0;
ll fin = -1;
struct node
{
    ll value;
    node *left, *right;
};

node *new_node(ll item)
{
    node *temp = (struct node *)malloc(sizeof(struct node));
    temp->value = item;
    temp->left = NULL;
    temp->left = NULL;
    return temp;
}

node *insert(node *node, ll value)
{
    if (node == NULL)
        return new_node(value);

    if (value < node->value)
        node->left = insert(node->left, value);

    else if (value > node->value)
        node->right = insert(node->right, value);

    return node;
}

void inorder(node *root, ll value)
{
    if (root == NULL)
        return;

    inorder(root->left, value);
    arr[ind] = root->value;
    if (arr[ind] == value)
        fin = ind;
    ind++;
    inorder(root->right, value);
}

int main()
{
    ll n;
    cin >> n;
    ll size = 0;
    node *root = NULL;
    while (n--)
    {
        ll operation, element;
        cin >> operation >> element;

        if (operation == 1)
        {
            root = insert(root, element);
            size += 1;
        }

        else
        {
            inorder(root, element);
            ll ans = fin;

            if (ans == -1)
                cout << "Data tidak ada" << endl;

            else
                cout << size - ans << endl;

            ind = 0;
            fin = -1;
        }
    }
    return 0;
}