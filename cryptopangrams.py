import math
def prime_factors(n):
    factors = []
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i == 0):
            factors.append(i)
            factors.append(n//i)
    factors.sort()
    # factors = factors[1:len(factors)-1]

    return(factors)

t = int(input())

for j in range(t):
    line = input().split() 
    k,n = int(line[0]),int(line[1])
    dict = {}
    arr = []
    line1 = input().split()
    for i in range(n):
        arr.append(int(line1[i]))

    primes = []
    for i in range(len(arr)):
        primes.extend(prime_factors(arr[i]))

    primes = list(set(primes))
    primes.sort()

    start = 65
    for i in range(len(primes)):
        dict[primes[i]] = chr(start)
        start+=1

    first = prime_factors(arr[0])
    first.sort()

    final = ""

    final += dict[first[0]]
    two = arr[0]//first[0]
    final += dict[two]
    next = two
    for i in range(1,len(arr)):
        new = arr[i]//next
        final+= dict[new]
        next = new

    print(("Case #%d: %s") % (j+1,final))

# import math
# def prime_factors(n):
#     factors = []
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n % i == 0):
#             factors.append(i)
#             factors.append(n//i)
#     factors.sort()
#     # factors = factors[1:len(factors)-1]
#
#     return(factors)
#
# t = int(input())
#
# for j in range(t):
#     line = input().split()
#     k,n = int(line[0]),int(line[1])
#     dict = {}
#     arr = []
#     line1 = input().split()
#     for i in range(n):
#         arr.append(int(line1[i]))
#
#     primes = []
#     for i in range(len(arr)):
#         primes.extend(prime_factors(arr[i]))
#
#     primes = list(set(primes))
#     primes.sort()
#     print(primes)
#
#     start = 65
#     for i in range(len(primes)):
#         dict[primes[i]] = chr(start)
#         start+=1
#
#     first = prime_factors(arr[0])
#     first.sort()
#
#     final = ""
#
#     final += dict[first[0]]
#     two = arr[0]//first[0]
#     final += dict[two]
#     next = two
#     for i in range(1,len(arr)):
#         new = arr[i]//next
#         final+= dict[new]
#         next = new
#
#     print(("Case #%d: %s") % (j+1,final))
