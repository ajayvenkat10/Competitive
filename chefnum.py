t = int(input())

for i in range(t):
    n = int(input())
    input_line = input().split()
    positive = 0
    negative = 0

    for i in range(n):
        if(int(input_line[i]) < 0):
            negative += 1
        else:
            positive += 1

    if(positive == 0):
        print(negative,negative)

    elif(negative == 0):
         print(positive,positive)

    else:
        print(max(positive,negative), min(positive,negative))
