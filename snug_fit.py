t = int(input())

for i in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    A.sort()
    B.sort()

    sum_of_diameters = 0
    for i in range(n):
        sum_of_diameters += min(A[i], B[i])

    print(sum_of_diameters)
