def subsequence(arr):
    greatest = 0
    count = 0
    i=0
    while(i<len(arr)):
        while(i<len(arr) and arr[i]==1):
            count+=1
            i+=1

        if(count>greatest):
            greatest=count
        count=0
        i+=1

    return(greatest)

line1 = input().split()

N = int(line1[0])
Q = int(line1[1])
K = int(line1[2])
arr = []

line2 = input().split()
for i in range(N):
    arr.append(int(line2[i]))

queries = input()
queries = queries[:Q]

count = 0
sub = []
for i in range(len(arr)):
    max_sub = subsequence(arr)
    if(max_sub>K):
        max_sub=K
    sub.append(max_sub)

    arr = arr[-1:]+arr[:-1]

pos = 0
for i in range(len(queries)):
    if(queries[i] == "!"):
        pos+=1

    else:
        ans = pos % len(arr)
        print(sub[ans])
