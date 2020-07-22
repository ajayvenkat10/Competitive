t = int(input())

for i in range(t):
    b = input()

    a = b[0]

    for i in range(1,len(b)-1,2):
        a = a + b[i]

    if(len(b) > 1):
        a += b[-1]

    print(a)

