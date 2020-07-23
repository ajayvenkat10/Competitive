import random
import math
from itertools import permutations

N = int(input())

Universal = []

for i in range(math.factorial(N)):
    Universal.append(0)

P = [i for i in range(1,N+1)]
possible_permutations = permutations(P)
possible_permutations = [i for i in possible_permutations]

link = dict(zip(possible_permutations,Universal))

for i in range(2000000):

    Q = P
    for i in range(N):
        j = random.randint(0,N-1)
        Q[i],Q[j] = Q[j],Q[i]

    link[tuple(Q)] += 1


print(link)
max_key = max(link, key=link.get)
min_key = min(link, key=link.get)

print(max_key)
print(min_key)
