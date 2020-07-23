import sys
n=int(raw_input(""))
R=[]
W=[]
for i in range(n):
    a=raw_input("")
    a=a.split()
    R.append(int(a[0]))
    W.append(int(a[1]))
    if(W[i]>10 and W[i]<0):
        print "NO"
        sys.exit()

count=0
if(W[0]==10 and len(W)>1):
    print "NO"
    sys.exit()

for i in range(1,len(R)):
    if(R[i]>=R[i-1] and W[i]>=W[i-1]):
        if(W[i]==10):
            if(i==len(W)):
                print "YES"
                # sys.exit()
            else:
                print "NO"
            sys.exit()

        elif(W[i]==W[i-1] and R[i]==R[i-1]):
            print "NO"
            sys.exit()

        else:
            count=count+1

    else:
        count=-1
        break


if(count==-1):
    print "NO"

else:
    print "YES"
