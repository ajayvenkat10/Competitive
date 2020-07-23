#include <bits/stdc++.h>
#include <math.h>
#define MAX 2005
using namespace std;

#define ARRAY_SIZE(arr) sizeof(arr)/sizeof(arr[0])

typedef struct node_t node_t;

struct node_t
{
	int data;
	int lCount;
	node_t* left;
	node_t* right;
};

node_t *insert_node(node_t *root, node_t* node)
{
	node_t *pTraverse = root;
	node_t *currentParent = root;

	while(pTraverse)
	{
		currentParent = pTraverse;

		if( node->data < pTraverse->data )
		{
			pTraverse->lCount++;
			pTraverse = pTraverse->left;
		}
		else
		{
			pTraverse = pTraverse->right;
		}
	}

	if( !root )
	{
		root = node;
	}
	else if( node->data < currentParent->data )
	{
		currentParent->left = node;
	}
	else
	{
		currentParent->right = node;
	}

	return root;
}

int k_smallest_element(node_t *root, int k)
{
	int ret = -1;

	if( root )
	{
		node_t *pTraverse = root;

		while(pTraverse)
		{
			if( (pTraverse->lCount + 1) == k )
			{
				ret = pTraverse->data;
				break;
			}
			else if( k > pTraverse->lCount )
			{
				k = k - (pTraverse->lCount + 1);
				pTraverse = pTraverse->right;
			}
			else
			{
				pTraverse = pTraverse->left;
			}
		}
	}

	return ret;
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin>>t;
	while(t--)
	{
		int n,k,i,j,m,index,f,flag = 0,count = 0;
		int arr[MAX];

		cin>>n>>k;

		for(i=0;i<n;i++)
			cin>>arr[i];

		for(i=0;i<n-1;i++)
		{	if(arr[i] > arr[i+1])
			{
				flag = 1;
				break;
			}
		}

		if(flag==0)
		{
			for(i=0;i<n;i++)
			{
				int sub_arr_per_i[n];
				int count_arr_per_i[MAX] = {0};
				int x = 0;
				for(j=i;j<n;j++)
				{
					sub_arr_per_i[x] = arr[j];
					x++;
					count_arr_per_i[arr[j]] += 1;
					m = k/x;
					if(k%x != 0)
						m += 1;
					index = k/m;
					if(k%m != 0)
						index += 1;
					index -= 1;

					f = count_arr_per_i[sub_arr_per_i[index]];
					if(count_arr_per_i[f])
						count += 1;
				}
			}
		}

		else
		{
			for(i=0;i<n;i++)
			{
				int sub_arr_per_i[n];
				int count_arr_per_i[MAX] = {0};
				int x = 0;
				int kth_ele = 0;
				node_t *root = NULL;
				for(j=i;j<n;j++)
				{
					sub_arr_per_i[x] = arr[j];
					x++;
					count_arr_per_i[arr[j]] += 1;
					m = k/x;
					if(k%x != 0)
						m += 1;
					index = k/m;
					if(k%m != 0)
						index += 1;

					node_t * new_node = (node_t *)malloc( sizeof(node_t) );
					new_node->data = arr[j];
					new_node->lCount = 0;
					new_node->left = NULL;
					new_node->right = NULL;

					root = insert_node(root, new_node);
					kth_ele = k_smallest_element(root,index);
					f = count_arr_per_i[kth_ele];
					if(count_arr_per_i[f])
						count += 1;

				}
			}
		}
		cout<<count<<endl;
	}
	return 0;
}
