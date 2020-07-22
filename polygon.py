t = int(input())

for i in range(t):
    n = int(input())

    matrix = []

    for i in range(n):
        row = input()
        matrix.append(list(row))


    ans = True 

    for i in range(n-1):
        for j in range(n-1):
            if(matrix[i][j] == "1"):
                if(matrix[i+1][j] == "1" or matrix[i][j+1] == "1"):
                    ans = True 

                else:
                    ans = False 
                    break 
        if(ans == False):
            break

    if(ans):
        print("YES")

    else:
        print("NO")

    
