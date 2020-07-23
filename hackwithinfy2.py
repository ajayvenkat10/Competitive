import math
def query1(a,b):
    print(a," ",b, flush=True)
    dist = int(input())
    return(dist)

def query2(a,b):
    print(a," ",b, flush=True)
    dist = input()
    return(dist)

def primeFactors(n):
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            prime_factors.append(i)
            n = n // i
    if n > 2:
        prime_factors.append(n)

t = int(input())
for i in range(t):
    prime_factors = []
    mid = 22361
    initial = pow(mid,2)
    first_result = query1(1,mid)
    prime_number = -1

    if(first_result == initial):
        maximum = 31623**2
        second_result = query1(1,31623)

        x = maximum - second_result

        if(x//2 > initial):
            prime_number = x//2

        else:
            prime_number = x

    else:
        number = initial - first_result
        primeFactors(number)
        final = []
        flag = 0
        magic_number = -1
        prime_factors = list(set(prime_factors))

        for i in range(1,31623):
            arr = []
            dict = {}
            for j in range(len(prime_factors)):
                y = pow(i,2)%prime_factors[j]
                arr.append(y)
                dict[y] = prime_factors[j]

            arr = list(set(arr))
            if(len(arr) == len(prime_factors)):
                flag = 1
                magic_number = i
                final = arr
                break

        second_result = query1(1,magic_number)

        prime_number = dict[second_result]

    answer = query2(2,prime_number)

    if(answer == "No"):
        break
