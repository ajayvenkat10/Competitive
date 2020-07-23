from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    number = input()
    dictionary = defaultdict(int)

    for i in range(n):
        dictionary[number[i]] += 1

    keys = list(dictionary.keys())

    odd = []
    for i in range(len(keys)):
        if(dictionary[keys[i]] %2 == 1):
            odd.append(keys[i])

    if(len(odd) == 0):
        print(-1)

    elif(len(odd) == 1):
        print(0)

    else:
        odd.sort()

        print(int(odd[-1]) - int(odd[-2]))
