t = int(input())
bit = 0
nibble = 0
byte = 0
for i in range(t):
    N = int(input())
    N = N-1

    if(N%26 < 2):
        bit = 2**(N//26)
        nibble = 0
        byte = 0

    elif(N%26 < 10):
        bit = 0
        nibble = 2**(N//26)
        byte = 0

    else:
        bit = 0
        nibble = 0
        byte = 2**(N//26)

    print (("%d %d %d") % (bit,nibble,byte))
