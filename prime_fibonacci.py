# import math
#
# def isPrime(num):
#     if(num < 2):
#         return(False)
#
#     for i in range(2, int(math.sqrt(num))+1):
#         if(num % i == 0):
#             return(False)
#     return(True)
#
# def fibonacci(a,b,length):
#     c = 0
#     for i in range(2,length):
#         c = a + b
#         a = b
#         b = c
#     return(c)
#
# line = input().split()
# n1,n2 = int(line[0]),int(line[1])
#
# primes1 = []
#
# for i in range(n1,n2+1):
#     if(isPrime(i)):
#         primes1.append(i)
#
# if(len(primes1) == 0):
#     ans = 0
#
# else:
#     primes2= []
#     for i in range(len(primes1)):
#         for j in range(len(primes1)):
#             if(i!=j):
#                 combination = int(str(primes1[i]) + str(primes1[j]))
#                 if(isPrime(combination)):
#                     primes2.append(combination)
#
#     primes2 = list(set(primes2))
#
#     if(len(primes2) == 0):
#         ans = 0
#     else:
#         x = min(primes2)
#         y = max(primes2)
#         ans = fibonacci(x,y,len(primes2))
#
# print(ans)

arr = list(map(int, input().split()))
print(arr)
