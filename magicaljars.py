t = int(input())

for i in range(t):
    n = int(input())
    A = []
    line = input().split()

    for i in range(n):
        A.append(int(line[i]))

    print(sum(A)-n+1)
