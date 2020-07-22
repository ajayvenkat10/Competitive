import math 

def findAllFactors(n):
    factors = []

    for i in range(1, int(math.sqrt(n))+1):
        if(n % i == 0):
            factors.append(i)
            factors.append(n//i)

    return factors

t = int(input())

for i in range(t):
    n,k = map(int, input().split())

    fact = findAllFactors(n)

    fact.sort()

    low = 0
    high = len(fact)-1

    while(low < high):
        mid = (low + high)//2

        if(fact[mid] >= k):
            high = mid

        else:
            low = mid + 1 


    print(n//fact[high])
