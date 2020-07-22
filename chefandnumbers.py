from collections import defaultdict

t = int(input())

def pair():
    return ([-1,0])

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    indices = defaultdict(pair)

    count = 1
    ans = 1005
    for i in range(n):
        if(indices[arr[i]][0] == -1):
            indices[arr[i]][0] = i
            indices[arr[i]][1] += 1

        else:
            if(i - indices[arr[i]][0] > 1):
                indices[arr[i]][0] = i
                indices[arr[i]][1] += 1
                
                if(indices[arr[i]][1] >= count):
                    if(indices[arr[i]][1] > count):
                        ans = arr[i]
                    else:
                        ans = min(ans, arr[i])

                    count = indices[arr[i]][1]
    
    if(ans == 1005):
        ans = min(arr)

    print(ans)

                
