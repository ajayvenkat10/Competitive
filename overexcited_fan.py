t = int(input())

for _ in range(t):
    x,y,directions = map(str, input().split())
    x = int(x)
    y = int(y)

    ans = -1

    if(x == 0 and y == 0):
        ans = 0

    else:
        for i in range(len(directions)):
            if(directions[i] == 'N'):
                y += 1
            if(directions[i] == 'S'):
                y -= 1
            if(directions[i] == 'E'):
                x += 1
            if(directions[i] == 'W'):
                x -= 1

            if(abs(x) + abs(y) <= i+1):
                ans = i+1 
                break 

    if(ans == -1):
        ans = "IMPOSSIBLE" 

    print("Case #%d: %s" % (_+1, ans))
          

