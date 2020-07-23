import math

t = int(input())
MAX = 1000000007
for i in range(t):
    n = int(input())
    arr = []
    fact = 1
    for i in range(1,n+2):
        fact = fact*i

    print((fact -1) % MAX)
    #
    # for i in range(1,n+1):
    #     arr.append(i)
    #
    # for i in range(n-1):
    #     x = arr[-2]
    #     y = arr[-1]
    #     z = x+y+(x*y)
    #
    #     arr.pop(-1)
    #     arr.pop(-1)
    #     arr.append(z)
    #
    # print(arr[0]%MAX)
