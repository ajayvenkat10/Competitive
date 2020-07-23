t = input().split()

n = int(t[0])
m = int(t[1])
a = int(t[2])

ans1=0
ans2=0

if(m ==a and n== a):
    print(1)

else:
    part1 = m//a
    part2 = n//a
    if(m%a == 0):
        ans1 = part1
    else:
        ans1 = part1 + 1

    if(n%a == 0):
        ans2 = part2

    else:
        ans2 = part2+1

    print(ans1*ans2)
