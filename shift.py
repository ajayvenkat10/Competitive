def shift(a):
    binary = "{0:b}".format(a)
    print(binary)
    lsb = binary[-1]
    print(lsb)
    a = a>>1
    print(a)
    shifted_binary = "{0:b}".format(a)
    shifted_binary = lsb+shifted_binary
    final = int(shifted_binary,2)
    return(final)

print(shift(362))
