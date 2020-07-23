t = int(input())

for i in range(t):
    n = int(input())
    attack = []
    defense = []
    line1 = input().split()
    line2 = input().split()

    for i in range(n):
        attack.append(int(line1[i]))
        defense.append(int(line2[i]))

    ans = -1

    for i in range(n):
        victim = defense[i]
        if(i==0):
            perp = attack[(i+1)%n] + attack[-1]

        else:
            perp =  attack[(i+1)%n] + attack[(i-1)%n]

        if(victim > perp):
            if(victim > ans):
                ans = victim

    print(ans)
