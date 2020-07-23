from collections import defaultdict
import math

t = int(input())

x_axis = defaultdict(int)
y_axis = defaultdict(int)
x = []
y = []
for i in range(t):
    n,m = map(int, input().split())
    x_axis[n] += 1
    y_axis[m] += 1
    x.append(n)
    y.append(m)

valid = 0
for i in range(t):
    valid += (x_axis[x[i]] - 1) * (y_axis[y[i]] - 1)

print(valid)
    #
    # flag1 = False
    # flag2 = False
    # zero = False
    # x = list(map(int, input().split()))
    # y = list(map(int, input().split()))
    # negative_x = 0
    # negative_y = 0
    # positive_x = 0
    # positive_y = 0
    # for i in range(n):
    #     if(x[i] < 0):
    #         x_axis[-x[i]] += 1
    #         negative_x += 1
    #     elif(x[i] > 0):
    #         x_axis[x[i]] += 1
    #         positive_x += 1
    #
    #     elif(x[i] == 0):
    #         zero = True
    #         x_axis[x[i]] += 1
    #         flag1 = True
    #
    # for i in range(m):
    #     if(y[i] < 0):
    #         y_axis[-y[i]] += 1
    #         negative_y += 1
    #
    #     elif(y[i] > 0):
    #         y_axis[y[i]] += 1
    #         positive_y += 1
    #
    #     elif(y[i] == 0):
    #         zero = True
    #         flag2 = True
    #
    # if(zero):
    #     if(flag1):
    #         n-=1
    #     if(flag2):
    #         m-=1
    #
    #     valid += (m*n)
    #
    # arr = [negative_x,positive_x,negative_y,positive_y]
    #
    # if(arr.count(0) <= 1):
    #     x_keys = list(x_axis.keys())
    #
    #     for i in range(len(x_keys)):
    #         valid += (x_axis[x_keys[i]]) * (y_axis[x_keys[i]])
    #
    # print(valid)
