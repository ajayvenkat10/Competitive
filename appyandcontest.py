from fractions import gcd

t = int(input())

for i in range(t):
    line = input().split()
    N = int(line[0])
    A = int(line[1])
    B = int(line[2])
    K = int(line[3])

    lcm = (A*B)//gcd(A,B)
    ans = ((N//A) + (N//B) - (2*(N//lcm)))

    if(ans>=K):
        print("Win")

    else:
        print("Lose")
