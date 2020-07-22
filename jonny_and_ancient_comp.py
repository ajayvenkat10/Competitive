t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    x = min(a, b)
    y = max(a, b)

    ans = -1
    count = 0
    if(y % x == 0):
        quo = y//x
        if(quo and (not(quo & (quo-1)))):
            quo = len(bin(quo)[2:]) - 1
            count += quo//3
            quo = quo % 3
            count += quo//2
            quo = quo % 2
            count += quo//1
            ans = count 
        else:
            ans = -1 

    print(ans)
