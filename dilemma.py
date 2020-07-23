t = int(input())

for i in range(t):
    cards = input()

    if(cards.count('1') % 2 == 1):
        print("WIN")

    else:
        print("LOSE")
