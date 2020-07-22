t  = int(input())

for i in range(t):
    n,m = map(int,input().split())
    matrix = []

    for i in range(n):
        rows = []
        line = input().split()
        for j in range(m):
            rows.append(int(line[j]))

        matrix.append(rows)

    east = []
    west = []
    north = []
    south = []

    initial_val = []
    for i in range(m):
        initial_val.append(0)

    for i in range(n):
        east.append(initial_val[:])
        west.append(initial_val[:])
        north.append(initial_val[:])
        south.append(initial_val[:])

    for i in range(n):
        east[i][0] = matrix[i][0]
        for j in range(1,m):
            east[i][j] = min(matrix[i][j] , matrix[i][j] + east[i][j-1])

    for i in range(n):
        west[i][-1] = matrix[i][-1]
        for j in range(m-2,-1,-1):
            west[i][j] = min(matrix[i][j] , matrix[i][j] + west[i][j+1])

    for i in range(m):
        north[-1][i] = matrix[-1][i]
        for j in range(n-2,-1,-1):
            north[j][i] = min(matrix[j][i], matrix[j][i] + north[j+1][i])

    for i in range(m):
        south[0][i] = matrix[0][i]
        for j in range(1,n):
            south[j][i] = min(matrix[j][i], matrix[j][i] + south[j-1][i])

    answers = []
    elements = 0
    for i in range(n):
        for j in range(m):
            elements = east[i][j] + west[i][j] + north[i][j] + south[i][j] - (3*matrix[i][j])
            answers.append(elements)
    
    print(min(answers))
