import math


def LCM(a, b):
    return (a * b)//math.gcd(a, b)


n = int(input())

arr = list(map(int, input().split()))

suffix_arr = [1] * n
suffix_arr[-1] = arr[n-1]

for i in range(n-2, -1, -1):
    suffix_arr[i] = math.gcd(arr[i], suffix_arr[i+1])

ans = LCM(arr[0], suffix_arr[1])

for i in range(1, n-1):
    ans = math.gcd(ans, LCM(arr[i], suffix_arr[i+1]))

print(ans)
