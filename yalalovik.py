import math
t = int(input())

for i in range(t):
    number = int(input())
    size = len(str(number))
    divisor = pow(10,size-1)
    ans  = str(number)

    for i in range(size-1):
        part1 = number%divisor
        part2 = number//divisor
        num = str(part1) + str(part2)
        ans = ans+num
        number = int(num)

    ans = int(ans)
    ans = ans % ((10**9)+7)
    print(ans)
