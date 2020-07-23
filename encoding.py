# # t = int(input())
# # MAX = 1000000007
# # for i in range(t):
# #     Nl,L = map(int, input().split())
# #     Nr,R = map(int, input().split())
# #
# #     sum = 0
# #     for i in range(L,R+1):
# #         x = list(str(i))
# #         num = x[0]
# #
# #         if(len(set(x)) == len(x)):
# #             sum += (i % MAX)
# #
# #         else:
# #             for j in range(1,len(x)):
# #                 if(x[j] != num):
# #                     num = x[j]
# #
# #                 else:
# #                     x[j] = '0'
# #
# #             sum += (int(''.join(x)) % MAX)
# #
# #     print(sum % MAX)
# import math
# prime_factors = []
# def primeFactors(n):
#     while n % 2 == 0:
#         prime_factors.append(2)
#         n = n // 2
#     for i in range(3,int(math.sqrt(n))+1,2):
#         while n % i== 0:
#             prime_factors.append(i)
#             n = n // i
#     if n > 2:
#         prime_factors.append(n)
#
# primeFactors(100)
# print(prime_factors)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getSubsets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER n
#  3. INTEGER_ARRAY arr
#
def primeFactors(n):
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            prime_factors.append(i)
            n = n // i
    if n > 2:
        prime_factors.append(n)
    return(list(set(prime_factors)))

def countWays(n, k):

    if (n == 0 or k == 0 or k > n):
        return 0
    if (k == 1 or k == n):
        return 1

    return (k * countWays(n - 1, k) +
                countWays(n - 1, k - 1))

def getSubsets(k, n, arr):
    # Write your code here
    print(arr)
    factors =[]
    total = 0
    for i in range(len(arr)):
        factors.extend(primeFactors(arr[i]))
    print(factors)

    total = (sum(factors)) % 1000000

    return((countWays(3,2)) % 1000000007)

if __name__ == '__main__':

    k = int(input().strip())

    n = int(input().strip())

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getSubsets(k, n, arr)

    print(result)
