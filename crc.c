#include<stdio.h>
#include<stdlib.h>

int generator[150],message[150],oper_arr[150];
int genlen,meslen,length;

void send()
{   int i,j,n;
    j = 0;
    i=0;
    printf("\nEnter the number of bits in the generator polynomial: ");
    scanf("%d",&genlen);
    printf("\nEnter the generator polynomial: ");
    for(i=0;i<genlen;i++)
        scanf("%d",&generator[i]);

    printf("\nEnter the number of bits in the message polynomial: ");
    scanf("%d",&meslen);
    printf("\nEnter the generator polynomial: ");
    for(i=0;i<meslen;i++)
        scanf("%d",&message[i]);

    length = genlen+meslen-1;

    for(i=meslen;i<length;i++)
        message[i]=0;

    n = genlen;

    for(i=0;i<genlen;i++)
        oper_arr[i] = message[i];

    while(n<=length)
    {
        if(oper_arr[0] == 1)
        {   for(i=0;i<genlen;i++)
                oper_arr[i] = oper_arr[i]^generator[i];
        }
        for(i=0;i<genlen-1;i++)
            oper_arr[i] = oper_arr[i+1];
        oper_arr[genlen-1] = message[n];
        n++;
    }
    // int j = 0;
    for(i=meslen;i<length;i++)
    {
        message[i] = oper_arr[j];
        j++;
    }
    printf("\n Message sent is: ");
    for(i=0;i<length;i++)
        printf("%d",message[i]);
}

void recieve()
{   int i,j,n;
    int flag = 0;
    for(i=0;i<genlen;i++)
        oper_arr[i] = message[i];
    n = genlen;

    while(n<=length)
    {
        if(oper_arr[0] == 1)
        {   for(i=0;i<genlen;i++)
                oper_arr[i] = oper_arr[i]^generator[i];
        }
        for(i=0;i<genlen-1;i++)
            oper_arr[i] = oper_arr[i+1];
        oper_arr[genlen-1] = message[n];
        n++;
    }
    printf("\n Result of division at reciever: ");
    for(i=0;i<genlen-1;i++)
    {
        printf("%d ",oper_arr[i]);
        if(oper_arr[i] == 1)
            flag = 1;
    }

    if(flag==1)
        printf("\nMessage has errors");
    else
        printf("\nMessage has no errors");
}

void error()
{
    int i,j,pos;
    printf("\nEnter the position in which error has to occur: ");
    scanf("%d",&pos);

    if(message[pos-1]==0)
        message[pos-1] = 1;
    else
        message[pos-1] = 0;

    printf("\nMessage to be sent: ");
    for(i=0;i<length;i++)
        printf("%d",message[i]);
    recieve();
}

int main()
{
    send();
    recieve();
    error();
    return 0;
}
