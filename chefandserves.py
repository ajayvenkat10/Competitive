t = int(input())

for i in range(t):
    input_line = input().split()

    P1 = int(input_line[0])
    P2 = int(input_line[1])
    K = int(input_line[2])

    num = P1+P2

    if((num//K)%2 == 0):
        print("CHEF")

    else:
        print("COOK")
