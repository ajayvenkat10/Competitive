def add(a,b):
    if(b==0):
        return(a)

    sum = a^b
    carry = (a&b)<<1
    print(sum,carry)
    return add(sum,carry)


print(add(5,3))
