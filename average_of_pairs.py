n= int(raw_input(""))
A=[]
Z=[]
sum=0
for i in range(n):
    A=[]
    sum=0
    a=int(raw_input(""))
    b=raw_input("")
    b=b.split()
    for i in range(a):
        A.append(int(b[i]))
    A.sort()
    count=0
    count1=0
    for i in range(len(A)-1):
        # print A[i]
        if(i>0):
            if(A[i]==A[i-1]):
                count1=count1+(sum-1)
                sum=sum-1
                # sum=sum-1
                # print "sum= %d" % sum
                # print "count1 = %d" % count1
                # print sum
                # print count1

            else:
                sum=0
                for j in range(i+1,len(A)):
                    if((A[i]%2==0 and A[j]%2==0) or (A[i]%2==1 and A[j]%2==1)):
                        d=A[i]
                        e=A[j]
                        x=(d+e)/2
                        count=0
                        low=i+1
                        high=len(A)-1
                        while(low<=high):
                            mid=(low+high)/2
                            # print A[mid]
                            if(A[mid]==x):
                                count=count+1
                                break
                            elif(A[mid]<x):
                                low=mid+1
                            else:
                                high=mid-1
                        if(count>0):
                            sum=sum+1
                # print "sum= %d" % sum
                count1=count1+sum
                # print "count1 = %d" % count1
        else:
            sum=0
            for j in range(i+1,len(A)):
                if((A[i]%2==0 and A[j]%2==0) or (A[i]%2==1 and A[j]%2==1)):
                    d=A[i]
                    e=A[j]
                    x=(d+e)/2
                    count=0
                    low=i+1
                    high=len(A)-1
                    while(low<=high):
                        mid=(low+high)/2
                        if(A[mid]==x):
                            count=count+1
                            break
                        elif(A[mid]<x):
                            low=mid+1
                        else:
                            high=mid-1
                    if(count>0):
                        sum=sum+1
            # print "sum= %d" % sum
            count1=count1+sum
            # print "count1 = %d" % count1

    Z.append(count1)

for i in range(len(Z)):
    print Z[i]
