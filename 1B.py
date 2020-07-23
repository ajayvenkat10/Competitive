t = int(input())

for j in range(t):
    line = input().split()
    P = int(line[0])
    Q = int(line[1])

    X = [0]*(Q+1)
    Y = [0]*(Q+1)

    for i in range(P):
        line1 = input().split()
        if(line1[2] == 'N'):
            for i in range(int(line1[1])+1,Q+1):
                Y[i] += 1
        elif(line1[2] == 'S'):
            for i in range(0,int(line1[1])):
                Y[i] += 1

        elif(line1[2] == 'W'):
            for i in range(0,int(line1[0])):
                X[i] += 1

        else:
            for i in range(int(line1[0])+1,Q+1):
                X[i] += 1

    ans_x = 0
    ans_y = 0
    val_x = 0
    val_y = 0
    for i in range(Q+1):
        if(X[i] > val_x):
            val_x = X[i]
            ans_x = i

        if(Y[i] > val_y):
            val_y = Y[i]
            ans_y = i

    print(("Case #%d: %d %d") % (j+1,ans_x,ans_y))
