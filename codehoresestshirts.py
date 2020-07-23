from collections import defaultdict

t = int(input())

previous = []
present = []
dict1 = defaultdict(int)
dict2 = defaultdict(int)

for i in range(t):
    word = input()
    previous.append(word)
    dict1[word] += 1

for i in range(t):
    word = input()
    present.append(word)
    dict2[word] += 1

intersection = list(set(previous) & set(present))

valid = 0
for i in range(len(intersection)):
    valid += min(dict1[intersection[i]],dict2[intersection[i]])

print(len(previous) - valid)
