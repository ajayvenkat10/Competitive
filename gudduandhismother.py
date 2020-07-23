from collections import defaultdict

def pair():
    return ([0,0])

def findSubsequences(sequence):
    dictionary = defaultdict(pair)
    xorResult = 0
    total = 0

    for i in range(len(sequence)):
        xorResult = xorResult ^ sequence[i]

        if(xorResult == 0):
            total += i

        tuple = dictionary[xorResult]

        if(tuple[1] > 0):
            total += ((tuple[1] * i) - (sum(tuple)))

        dictionary[xorResult][0] += i
        dictionary[xorResult][1] += 1

    return(total)

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = findSubsequences(arr)

    print(ans)
