# from fractions import gcd
#
# def gcd_n(numbers):
#     return reduce(lambda x, y: gcd(x, y), numbers)
#
#
# A=[10,15,30]
# print gcd_n(A)

from functools import reduce

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))


# A=[20,40,60]
X=[]
A=factors(20)
B=factors(40)
C=factors(60)
X.append(A)
X.append(B)
X.append(C)
# print X
print(A)
print(B)
# print C

Z=set.intersection(*X)
Z=list(Z)
print(Z)
