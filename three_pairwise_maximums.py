t = int(input())

for i in range(t):
    x,y,z = map(int, input().split())

    a = set([x,y,z])

    ans = "NO"
    ans_arr = []

    if(len(a) == 1):
        ans = "YES"
        ans_arr = [x] * 3

    elif(len(a) == 2):
        lis = list(a)
        mini = min(lis)
        maxi = max(lis)

        tot = [x,y,z]
        min_count = tot.count(mini)
        max_count = tot.count(maxi)

        if(max_count > min_count):
            ans = "YES"
            ans_arr = [mini, mini, maxi]

    if(ans == "YES"):
        print(ans)
        print(*ans_arr)

    else:
        print(ans)

        
