from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
A = []
def prime_factors(number):
    A = list(factors(number))
    A.sort()
    # print(A)
    count = 0
    prime = True
    for i in range(1,len(A)):
        for j in range(2,A[i]):
            if(A[i]%j == 0):
                prime = False
                break

        if(prime):
            # print(A[i])
            count+=1
    return count

test_cases = int(input(""))

for i in range(test_cases):
    a = input("")
    a = a.split()
    n = int(a[0])
    m = int(a[1])
    sum = 0
    for i in range(n,m):
        sum += prime_factors(i)

    print(sum)
