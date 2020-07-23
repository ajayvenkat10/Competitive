t = int(input())

for i in range(t):
    members = []
    for i in range(3):
        A = []
        values = input().split()
        for i in range(3):
            A.append(int(values[i]))

        members.append(A)

    members.sort()

    ans =  True
    for i in range(len(members)-1):
        if(sum(members[i]) < sum(members[i+1])):
            for j in range(3):
                if(members[i][j] > members[i+1][j]):
                        ans = False
                        break
        else:
            ans = False

    if(ans):
        print("yes")

    else:
        print("no")
