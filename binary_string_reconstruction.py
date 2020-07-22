t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())

    zeros = 0
    zero_ones = 0
    ones = 0
    addend = False

    if(a > 0):
        if(b == 0 and c == 0):
            zeros = a + 1

        elif(c == 0):
            zeros = a
            zero_ones = b + 1

        else:
            zeros = a
            zero_ones = b
            ones = c
            if(b % 2 == 1):
                zero_ones += 1
            else:
                addend = True 

    elif(c > 0):
        if(b == 0):
            ones = c + 1

        else:
            zero_ones = b
            ones = c
            if(b % 2 == 1):
                zero_ones += 1
            else:
                addend = True

    else:
        zero_ones = b + 1

    bridge = ""
    for i in range(zero_ones):
        if(i % 2 == 0):
            bridge += "0"
        else:
            bridge += "1"

    ans = ("0" * zeros) + bridge + ("1" * ones)

    if(addend):
        ans += "0"

    print(ans)
