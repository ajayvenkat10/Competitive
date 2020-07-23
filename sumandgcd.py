from fractions import gcd
T = int(input())

for i in range(T):
    n = int(input())
    sequence = list(map(int,input().split()))
    set_of_sequence = list(set(sequence))
    answer = 0
    if(len(set_of_sequence) == 1):
        answer = set_of_sequence[0] + set_of_sequence[0]

    elif(len(set_of_sequence) == 2):
        answer = set_of_sequence[0] + set_of_sequence[1]

    else:
        final = []
        highest = max(set_of_sequence)
        x = list(set(set_of_sequence) - {highest})
        second_highest = max(x)

        best_of_two = [second_highest,highest]

        for i in range(len(best_of_two)):
            num = best_of_two[i]
            reduced_set_of_sequence = list(set(set_of_sequence) - {num})
            HCF = reduced_set_of_sequence[0]

            for j in range(1,len(reduced_set_of_sequence)):
                HCF = gcd(HCF,reduced_set_of_sequence[j])

            final.append(HCF+num)

        answer = max(final)

    print(answer)
