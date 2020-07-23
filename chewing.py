t = input("")
t = t.split()

N = int(t[0])
K = int(t[1])

hardness_quotient = []

a = input("")
a = a.split()
for i in range(N):
    elements = int(a[i])
    hardness_quotient.append(elements)

hardness_quotient.sort()

if(hardness_quotient[0]>=K):
    print(0)

else:
    low = 0
    high = N-1

    while(low<=high) :
        mid = int((low+high)/2)
        if(hardness_quotient[mid]<K):
            if(mid == N-1 or hardness_quotient[mid+1]>=K):
                pos = mid
                break
            else:
                low = mid+1

        else:
            high = mid-1

    hardness_quotient = hardness_quotient[:pos+1]

    if(len(hardness_quotient)==1):
        print(0)

    else:
        pairs = 0
        for i in range(len(hardness_quotient)):
            low = i
            high = len(hardness_quotient)-1
            while low<high:
                mid=int((low+high)/2)
                if(hardness_quotient[mid]+hardness_quotient[i]>=K):
                    high=mid
                else:
                    low=mid+1
            if(i!=low):
                pairs += (low-i)
                if(hardness_quotient[i]+hardness_quotient[low] >= K):
                    pairs -= 1

        print(pairs)
