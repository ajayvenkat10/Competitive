import math
from collections import defaultdict

def Factors(n) :
    arr = []
    for i in range(1,int(math.sqrt(n))+1):
        if (n % i == 0) :
            if (n // i == i) :
                arr.append(i)

            else :
                arr.append(i)
                arr.append(n//i)

    return (arr)

t = int(input())

for i in range(t):
    n = int(input())
    index = defaultdict(int)
    dict = defaultdict(int)
    count_dict  = defaultdict(int)

    numbers = list(map(int, input().split()))

    for i in range(n):
        index[numbers[i]] = i
        dict[numbers[i]] += 1

    for i in range(n-1):
        factors = Factors(numbers[i])
        for j in range(len(factors)):
            if(dict[factors[j]]):
                if(index[factors[j]] > i):
                    count_dict[factors[j]] += 1

    keys = list(count_dict.keys())

    for i in range(len(keys)):
        count_dict[keys[i]] += min(0, dict[keys[i]]-1)

    count = list(count_dict.values())

    if(count_dict == {}):
        print(0)

    else:
        print(max(count))
