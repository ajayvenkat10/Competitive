# from collections import defaultdict

# t = int(input())

# for i in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     ori = defaultdict(bool)
#     dup = defaultdict(bool)

#     xor_result = 0

    
#     for i in range(n):
#         ori[arr[i]] = True
#         xor_result ^= arr[i]

#     if(xor_result == 0):
#         if(ori[0]):
#             arr.sort()
#             if(n > 1):
#                 ans = arr[1]
#             else:
#                 ans = -1
#         else:
#             ans = -1

#     else:
#         flag = True 
#         for i in range(n):
#             val = xor_result ^ arr[i]
#             if(ori[val]):
#                 if(dup[val]):
#                     flag = False 
#                     break 
#                 else:
#                     dup[val] = True 
#             else:
#                 flag = False 
#                 break 

#         if(flag):
#             ans = xor_result
#         else:
#             ans = -1

#     print(ans)

diff = []
tot = 0
for i in range(1,129):
    v = bin(i^ (i-1)).count('1')
    diff.append(v)
    tot += v

t = int(input())

for i in range(t):
    n = int(input())

    x = n//128

    part1 = (tot * x) + (x//2)

    part2 = sum(diff[:(n%128)])

    ans = part1+part2

    print(ans)
