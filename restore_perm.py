t = int(input())

for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    x = set()
    ans = []

    length = len(x)
    for i in range(n*2):
        x.add(arr[i])
        if(len(x) > length):
            ans.append(arr[i])
        length = len(x)
        
    print(* ans)