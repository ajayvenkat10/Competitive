from collections import defaultdict
t = int(input())

for i in range(t):
    n,k = map(int, input().split())
    indices = defaultdict(list)
    
    arr = list(map(int, input().split()))

    sorted_arr = arr[:]
    sorted_arr.sort()

    for i in range(n):
        indices[sorted_arr[i]].append(i)

    ans = True 

    for i in range(n):
        flag = False
        for j in range(len(indices[arr[i]])):
            if(abs(i - indices[arr[i]][j]) % k == 0):
                del(indices[arr[i]][j])
                flag = True 
                break
    
        if(flag == False):
            ans = False
            break

    if(ans):
        print("yes")

    else:
        print("no")