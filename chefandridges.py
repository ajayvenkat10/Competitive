from fractions import Fraction

line = input().split()
t = int(line[0])
A = []
for i in range(1,t+1):
    n = int(line[i])
    arr = [0,1]

    for i in range(2,(2*n)+1):

        if(i%2 == 0):
            arr.append(2**(i//2))

        else:
            arr.append(arr[i-1]-arr[i-2])

    A.append(arr[-2])
    A.append(arr[-1])

print(*A)
