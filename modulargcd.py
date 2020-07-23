from fractions import gcd

t = int(input(""))

for i in range(t):
    input_line = input("")
    input_line = input_line.split()

    A = int(input_line[0])
    B = int(input_line[1])
    N = int(input_line[2])

    if(A==B):
        ans = A**N + B**N

    else:

        par1 = pow(A,N,(A-B))
        par2 = pow(B,N,(A-B))
        first_par = par1+par2
        second_par = abs(A-B)

        ans = gcd(first_par,second_par)

    print(ans % (10**9+7))
