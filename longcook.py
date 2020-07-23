# import math
#
# def dayofweek(d, m, y):
#     t = [ 0, 3, 2, 5, 0, 3,
#           5, 1, 4, 6, 2, 4 ]
#     y -= m < 3
#     return (( y + (y // 4) - (y // 100)
#              + (y // 400) + t[m - 1] + d) % 7)
#
# def isLeap(year):
#     if(year % 4 == 0):
#         if(year % 100 == 0):
#             if(year % 400 == 0):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# interval = []
# for i in range(1,401):
#     day = dayofweek(1,2,i)
#     if(isLeap(i)):
#         if(day == 6):
#             interval.append(1)
#         else:
#             interval.append(0)
#
#     else:
#         if(day == 0 or day == 6):
#             interval.append(1)
#         else:
#             interval.append(0)
#
# t = int(input())
#
# for i in range(t):
#     m1,y1 = map(int, input().split())
#     m2,y2 = map(int, input().split())
#
#     overlap = 0
#
#     if(m1 > 2):
#         y1 += 1
#
#     if(m2 >= 2):
#         y2 += 1
#
#
#     inter1 = 400 * (y1//400)
#     inter2 = 400 * (y2//400)
#
#     if(inter1 == inter2):
#         overlap += sum()
#
#     else:
#
#         overlap += sum(interval[400-(inter-y1)-1:])
#
#         diff = (y2 - inter)
#
#         quotient = diff//400
#         remainder = diff%400
#
#         overlap += (sum(interval) * quotient) + sum(interval[:remainder])
#
#     print(overlap)
#
#         # print(400-(inter-y1) , 400-(inter-y2))
#         # print("Yes")
#         # print(y1,y2)
#         # print(interval[400-(inter-y1)-1: 400-(inter-y2)])
#
#     # diff = (y2 - y1)
#     #
#     # quotient = diff//400
#     # remainder = diff%400
#     #
#     # overlap = (sum(interval) * quotient) + sum(interval[:remainder])
#     # print(overlap)


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


interval = []
for i in range(1,401):
    day = dayofweek(1,2,i)
    if(isLeap(i)):
        if(day == 6):
            interval.append(1)
        else:
            interval.append(0)

    else:
        if(day == 0 or day == 6):
            interval.append(1)
        else:
            interval.append(0)

t = int(input())

for i in range(t):
    m1,y1 = map(int, input().split())
    m2,y2 = map(int, input().split())

    overlap = 0

    if(m1 > 2):
        y1 += 1

    if(m2 < 2):
        y2 -= 1


    inter = 400 * math.ceil(y1/400)

    if(inter > y2):
        overlap += sum(interval[400-(inter-y1)-1: 400-(inter-y2)])

    else:

        overlap += sum(interval[400-(inter-y1)-1:])

        diff = (y2 - inter)

        quotient = diff//400
        remainder = diff%400

        overlap += (sum(interval) * quotient) + sum(interval[:remainder])

    print(overlap)
