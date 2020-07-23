# from collections import defaultdict
# n  = int(input())
#
# points = defaultdict(int)
# goal_diff = defaultdict(int)
# goals_scored = defaultdict(int)
# for i in range((n*(n-1))//2):
#     line = input().split()
#     if(int(line[2]) > int(line[3])):
#         points[line[0]] += 3
#     elif(int(line[2]) < int(line[3])):
#         points[line[1]] += 3
#
#     else:
#         points[line[0]] += 1
#         points[line[1]] += 1
#
#     goals_scored[line[0]] += int(line[2])
#     goals_scored[line[1]] += int(line[3])
#     goal_diff[line[0]] += int(line[2]) - int(line[3])
#     goal_diff[line[1]] += int(line[3]) - int(line[2])
#
# teams = list(points.keys())
# table = []
# for i in teams:
#     table.append((i,points[i],goal_diff[i],goals_scored[i]))
#
# def sec(val):
#     return (val[1:4])
#
# table.sort(reverse=True, key=sec)
#
# arr = []
#
# for i in range(n//2):
#     arr.append(table[i])
#
# def s(val):
#     return(val[0])
#
# arr.sort(key=s)
#
# for i in range(n//2):
#     print(int(arr[i][0]))

from collections import defaultdict
n  = int(input())

points = defaultdict(int)
goal_diff = defaultdict(int)
goals_scored = defaultdict(int)
for i in range((n*(n-1))//2):
    line = input().split()
    if(int(line[2]) > int(line[3])):
        points[line[0]] += 3
    elif(int(line[2]) < int(line[3])):
        points[line[1]] += 3

    else:
        points[line[0]] += 1
        points[line[1]] += 1

    goals_scored[line[0]] += int(line[2])
    goals_scored[line[1]] += int(line[3])
    goal_diff[line[0]] += int(line[2]) - int(line[3])
    goal_diff[line[1]] += int(line[3]) - int(line[2])

teams = list(points.keys())
table = []
for i in teams:
    table.append((points[i],goal_diff[i],goals_scored[i],int(i)))

table.sort(reverse=True)

arr = []
for i in range(n//2):
    arr.append(table[i][3])

arr.sort()
for i in range(len(arr)):
    print(int(arr[i]))
