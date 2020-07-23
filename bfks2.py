# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     num_sum = n
#     while(True):
#         if(num_sum%10 == num_sum):
#             break
#         else:
#             num_sum = str(num_sum)
#             num_sum = list(num_sum)
#             for i in range(len(num_sum)):
#                 num_sum[i] = int(num_sum[i])
#             num_sum = sum(num_sum)
#
#     answer = (10*n) + (10 - num_sum)
#
#     print(answer)

T = int(input())

while(T):
    T-=1
    n = int(input())

    num_sum = list(str(n))
    num_sum = sum(list(map(int,num_sum)))
    part1 = 10*n
    if(num_sum % 10 == 0):
        answer = part1
    else:
        part2 = 10 - (num_sum % 10)
        answer = part1 + part2

    print(answer)
