from collections import defaultdict

MOD = 998244353

t = int(input())

for _ in range(t):

    n = int(input())
    sequence = list(map(int, input().split()))
    frequency = defaultdict(int)

    for i in range(n):
        frequency[min(sequence[i], n+1)] += 1

    sequence_length_covered = 0
    sum_of_all_mex = 0
    permutation_of_all_smaller_values = 1

    for i in range(1, n+2):

        sequence_length_covered += frequency[i]
        sum_of_all_mex += (((pow(2, n-sequence_length_covered, MOD)
                           * i) % MOD )* permutation_of_all_smaller_values) % MOD

        if(frequency[i] == 0):
            break
        else:
            permutation_of_all_smaller_values *= (pow(2, frequency[i], MOD) - 1) % MOD

    print(sum_of_all_mex % MOD)
