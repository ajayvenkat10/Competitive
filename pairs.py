from collections import defaultdict

n = int(input())
arr = input().split()
dict =  defaultdict(int)

for i in range(n):
    dict[arr[i]] += 1

keys = list(dict.values())

pairs = 0

for i in range(len(keys)):
    pairs += keys[i]//2

print(pairs)
