t = int(input(""))
Z = []
for i in range(t):
    S = []
    line = input("")
    line = line.split()
    N = int(line[0])
    A = int(line[1])
    B = int(line[2])

    n = input("")
    n = n.split()
    for i in range(N):
        S.append(int(n[i]))

    first_prob = S.count(A)/(float(N))
    second_prob = S.count(B)/(float(N))

    prob = first_prob * second_prob

    Z.append(prob)

for i in range(len(Z)):
    print(Z[i])
