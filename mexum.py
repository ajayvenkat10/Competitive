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

    for i in range(1,n+1):
        sequence_length_covered += frequency[i]
        



