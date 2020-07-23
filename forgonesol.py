t = int(input())

for j in range(t):
    n = input()
    number = int(n)

    n = list(n)

    for i in range(len(n)):
        if(n[i] == '4'):
            n[i] = str(int(n[i]) - 1)

    n = ''.join(n)
    part1 = int(n)

    part2 = number - part1

    print(("Case #%d: %d  %d") % (j+1,part1,part2))
