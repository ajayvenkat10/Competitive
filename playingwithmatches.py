from collections import defaultdict

t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    matches = [6,2,5,5,4,5,6,3,7,6]

    sum1 = a+b
    sum1 = str(sum1)

    total = 0
    for i in range(len(sum1)):
        total += matches[int(sum1[i])]

    print(total)
