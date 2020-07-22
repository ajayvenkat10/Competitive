t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if(a >= b*2):
        ans = pow(a, 2)

    elif(b >= a*2):
        ans = pow(b, 2)

    else:
        ans = pow(min(a, b) * 2, 2)

    print(ans)
