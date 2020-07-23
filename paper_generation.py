import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return (numer // denom)

print(ncr(8,3) * ncr(5,2))
# n1 = int(input())
# m1 = int(input())
# n2 = int(input())
# m2 = int(input())
# n3 = int(input())
# m3 = int(input())
#
# answer1 = ncr(n1,m1) * ncr(n2,m2) * ncr(n3,m3)
#
# query1 = input().split()
# x = ord(query1[0]) - 64
# y = ord(query1[1]) - 64
#
# query2 = input()
# z = ord(query2) - 64
#
# if(x <= n1):
#     x_index = 1
# elif(x <= n1+n2):
#     x_index = 2
# else:
#     x_index = 3
#
# if(y <= n1):
#     y_index = 1
# elif(y <= n2+n1):
#     y_index = 2
# else:
#     y_index = 3
#
# if(z <= n1):
#     z_index = 1
# elif(z <= n2+n1):
#     z_index = 2
# else:
#     z_index = 3
#
# if(z_index == 1):
#     part1 = ncr(n1-1,m1-1) * ncr(n2,m2) * ncr(n3,m3)
# elif(z_index == 2):
#     part1 = ncr(n1,m1) * ncr(n2-1,m2-1) * ncr(n3,m3)
# else:
#     part1 = ncr(n1,m1) * ncr(n2,m2) * ncr(n3-1,m3-1)
#
# if(z_index == 1):
#     if(x_index == 1):
#         n1 -= 1
#         m1 -= 1
#     if(x_index == 2):
#         n2 -= 1
#         m2 -= 1
#     if(x_index == 2):
#         n3 -= 1
#         m3 -= 1
#     if(y_index == 1):
#         n1 -=1
#         m1 -= 1
#     if(y_index == 2):
#         n2 -=1
#         m2 -= 1
#     if(y_index == 3):
#         n3 -=1
#         m3 -= 1
#
#     part2 = ncr(n1-1,m1) * ncr(n2,m2) * ncr(n3,m3)
#
# elif(z_index == 2):
#     if(x_index == 1):
#         n1 -= 1
#         m1 -= 1
#     if(x_index == 2):
#         n2 -= 1
#         m2 -= 1
#     if(x_index == 2):
#         n3 -= 1
#         m3 -= 1
#     if(y_index == 1):
#         n1 -=1
#         m1 -= 1
#     if(y_index == 2):
#         n2 -=1
#         m2 -= 1
#     if(y_index == 3):
#         n3 -=1
#         m3 -= 1
#
#     part2 = ncr(n1,m1) * ncr(n2-1,m2) * ncr(n3,m3)
#
# else:
#     if(x_index == 1):
#         n1 -= 1
#         m1 -= 1
#     if(x_index == 2):
#         n2 -= 1
#         m2 -= 1
#     if(x_index == 2):
#         n3 -= 1
#         m3 -= 1
#     if(y_index == 1):
#         n1 -=1
#         m1 -= 1
#     if(y_index == 2):
#         n2 -=1
#         m2 -= 1
#     if(y_index == 3):
#         n3 -=1
#         m3 -= 1
#
#     part2 = ncr(n1,m1) * ncr(n2,m2) * ncr(n3-1,m3)
#
# print(answer1)
# print(answer1 - part1 - part2 + 1)
