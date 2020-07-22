t = int(input())

for i in range(t):

    n,s = map(int, input().split())

    player_val = list(map(int, input().split()))
    player_type = list(map(int, input().split()))

    defender = []
    forward = []

    for i in range(n):
        if(player_type[i] == 0):
            defender.append(player_val[i])
        else:
            forward.append(player_val[i])

    if(len(defender) > 0 and len(forward) > 0):

        if(min(forward) + min(defender) <= 100-s):
            print("yes")

        else:
            print("no")

    else:
        print("no")