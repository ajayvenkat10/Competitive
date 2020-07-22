#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *right;
    struct node *left;
};
struct node * create()
{
    struct node *newnode;
    int i;
    newnode=(struct node *)malloc(sizeof(struct node));
    printf("enter the data(-1 for no node)\n");
    scanf("%d",&i);
    if(i==-1)
    {
        return 0;
    }
    newnode -> data = i;
    printf("\nenter the left of the node %d\n",i);
    newnode->left=create();
    printf("\nEnter the right side of the node %d\n",i);
    newnode->right=create();
    return newnode;
}
void inorder(struct node *root)//here we have the structure which is passed here//
{
    if(root==0)
    {
        return;
    }
    inorder(root->left);
    printf("%d\t",root->data);
    inorder(root->right);
}
void postorder(struct node *root)
{
    if(root==NULL)
    {
        return;
    }
    postorder(root->left);
    postorder(root->right);
    printf("%d\t",root->data);
}
void preorder(struct node *root)
{
    if(root==NULL)
    {
        return;
    }
    printf("%d\t",root->data);
    preorder(root->left);
    preorder(root->right);
    
}
int main()
{
    struct node *root;
    root=0;
    root=create();
    printf("\nPre-Order traversal\n");
    preorder(root);
    printf("\n");
    printf("Post-Order traversal\n");
    postorder(root);
    printf("\n");
    printf("In-Order traversal\n");
    inorder(root);
    
}