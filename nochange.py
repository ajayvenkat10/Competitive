# import math
# from collections import defaultdict
#
# t = int(input())
#
# for i in range(t):
#     n,p = map(int, input().split())
#     rupees = list(map(int, input().split()))
#     hashmap = defaultdict(int)
#     check1 = defaultdict(int)
#     check2 = defaultdict(int)
#
#     rupees_copy = rupees[:]
#     rupees_copy.sort(reverse = True)
#
#     flag = False
#     pos = -1
#     ans_list = [0] * n
#     if(p % rupees_copy[0] == 0):
#         for i in range(1,n):
#             if(rupees_copy[i-1] % rupees_copy[i] != 0):
#                 flag = True
#                 pos = i
#                 break
#
#         if(flag):
#             ans = "YES"
#
#             for i in range(pos):
#                 if(check1[rupees_copy[i]] == 0):
#                     quotient = (p//rupees_copy[i]) - 1
#                     check1[rupees_copy[i]] = 1
#                     hashmap[rupees_copy[i]] = quotient
#                     p -= (rupees_copy[i] * quotient)
#
#             hashmap[rupees_copy[pos]] = math.ceil(p/rupees_copy[pos])
#
#             for i in range(n):
#                 if(check2[rupees[i]] == 0):
#                     check2[rupees[i]] = 1
#                     ans_list[i] = hashmap[rupees[i]]
#
#             print(ans, *ans_list)
#
#         else:
#             ans = "NO"
#             print(ans)
#
#     else:
#         ans = "YES"
#         hashmap[rupees_copy[0]] = math.ceil(p/rupees_copy[0])
#         for i in range(n):
#             if(check2[rupees[i]] == 0):
#                 check2[rupees[i]] = 1
#                 ans_list[i] = hashmap[rupees[i]]
#         print(ans, *ans_list)


import math

def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + (y // 4) - (y // 100)
             + (y // 400) + t[m - 1] + d) % 7)

def isLeap(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

t = int(input())

for i in range(t):
    m1,y1 = map(int, input().split())
    m2,y2 = map(int, input().split())

    interval = []
    overlap = 0

    if(m1 > 2):
        y1 += 1

    if(m2 >= 2):
        y2 += 1

    day = dayofweek(1,2,1)

    for i in range(1, 28):
        if(isLeap(i)):
            if(day == 6):
                interval.append(1)
            else:
                interval.append(0)
            day = (day + 366)% 7
        else:
            if(day == 0 or day == 6):
                interval.append(1)
            else:
                interval.append(0)
            day = (day + 365)% 7

    print(interval)
    inter = 28 * math.ceil(y1/28)

    if(inter > y2):
        print(28-(inter-y1) , 28-(inter-y2))
        overlap += sum(interval[28-(inter-y1): 28-(inter-y2)])

    else:
        overlap += sum(interval[28-(inter-y1):])

        diff = (y2 - inter)

        overlap += sum(interval[28-(inter-y1):])

        quotient = diff//28
        remainder = diff%28

        overlap += (sum(interval) * quotient) + sum(interval[:remainder])

    print(overlap)
