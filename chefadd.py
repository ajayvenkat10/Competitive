# def shift(a):
#     binary = "{0:b}".format(a)
#     lsb = binary[-1]
#     shifted = a>>1
#     shifted_binary = "{0:b}".format(shifted)
#     binary_list = list(shifted_binary)
#     binary_list[0] = lsb
#     final = int("".join(binary_list),2)
#     return(final)

def shift(a):
    binary = "{0:b}".format(a)
    print(binary)
    lsb = binary[-1]
    print(lsb)
    shifted_binary = lsb + binary[:len(binary)-1]
    print(shifted_binary)
    final = int(shifted_binary,2)
    print(final)
    return(final)

t = int(input())

for i in range(t):
    line = input().split()
    A = int(line[0])
    B = int(line[1])
    C = int(line[2])

    count = 1
    x = A
    # y = B
    while(1):
        x = shift(x)
        # y = shift(y)

        if(x==A ):#or y==B):
            break
        # else:
        #     if(x+y == C):
        #         count+=1

    print(count)
