import math
t = int(input())

arr = []
half_arr = []
e = 0
o = 0

for i in range(t):
    n = int(input())

    arr.append(n)
    half_arr.append(n//2)

diff = sum(half_arr)

if(diff < 0):
    for i in range(len(arr)):
        if(arr[i] %2 == 1):
            half_arr[i] += 1
            diff += 1
        if(diff == 0):
            break

for i in range(t):
    print(half_arr[i])
