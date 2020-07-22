t = int(input())

for i in range(t):
    n = int(input())
    candies = list(map(int, input().split()))

    alice_pointer = 0
    bob_pointer = n-1
    alice_current = 0
    bob_current = 0
    alice = 0
    bob = 0
    toggle = False
    number_of_moves = 0

    while(alice_pointer <= bob_pointer):
        if(toggle == False):
            alice_current += candies[alice_pointer]
            if(alice_current > bob_current):
                alice += alice_current
                bob_current = 0
                toggle = True
                number_of_moves += 1

            alice_pointer += 1

        else:
            bob_current += candies[bob_pointer]
            if(bob_current > alice_current):
                bob += bob_current
                alice_current = 0
                toggle = False
                number_of_moves += 1

            bob_pointer -= 1

    if(toggle):
        bob += bob_current
    else:
        alice += alice_current

    if(alice_current != 0 and bob_current != 0):
        number_of_moves += 1

    print(number_of_moves, alice, bob)
