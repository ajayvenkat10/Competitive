t = int(input())

for i in range(t):
    n = int(input())
    Universal = []
    A = []
    D = {}
    line = input().split()
    for i in range(n):
        A.append(int(line[i]))

    for i in range(max(n,max(A))+1):
        Universal.append(0)

    for i in range(len(A)):
        D[A[i]] = []

    for i in range(len(A)):
        Universal[A[i]] += 1
        D[A[i]].append(i+1)

    A_set_list = list(set(A))

    new_list = []
    for i in range(len(A_set_list)):
        if(Universal[A_set_list[i]] >= 2):
            new_list.append(A_set_list[i])
    ans = False
    for i in range(len(new_list)):
        x = []
        pos = D[new_list[i]]

        for i in range(len(pos)):
            if(Universal[pos[i]] > 0):
                x.append(pos[i])

        if(len(x) >= 2):
            ans = True
            break

    if(ans):
        print("Truly Happy")

    else:
        print("Poor Chef")
