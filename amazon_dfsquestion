def isSafe(Matrix, row, col, visited):
    global rows, columns
    return ((row >= 0) and (row < rows) and
            (col >= 0) and (col < columns) and
            (Matrix[row][col] and not visited[row][col]))

def DFS(Matrix, row, col, visited, count):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[row][col] = True

    for k in range(8):
        if (isSafe(Matrix, row + rowNbr[k],
                   col + colNbr[k], visited)):

            count[0] += 1
            DFS(Matrix, row + rowNbr[k],
                col + colNbr[k], visited, count)

def largestRegion(Matrix):
    global rows, columns
    visited = [[0] * columns for i in range(rows)]

    result = -1
    for i in range(rows):
        for j in range(columns):
            if (Matrix[i][j] and not visited[i][j]):
                count = [1]
                DFS(Matrix, i, j, visited , count)

                result = max(result , count[0])
    return result

rows = int(input())
columns = int(input())

matrix = []
for i in range(rows):
    line = list(map(int,input().split()))
    matrix.append(line)

print(largestRegion(matrix))
