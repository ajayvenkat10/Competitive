# def sum_digits(n):
#     s = 0
#     while n:
#         s += n % 10
#         n //= 10
#     return s

t = int(input())

for i in range(t):
    d = int(input())

    ans =  (d%9)+1
    #
    # while(len(str(ans))>1):
    #
    #     ans = sum_digits(ans)

    print(ans)
