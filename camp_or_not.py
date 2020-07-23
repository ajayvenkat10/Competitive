t = int(input())

for i in range(t):
    D = int(input())
    day_no = []
    problems_solved = []
    for i in range(32):
        day_no.append(0)

    for i in range(D):
        line1 = input().split()
        day_no[int(line1[0])] = int(line1[1])

    Q  = int(input())
    day = []
    problem = []
    for i in range(32):
        day.append(0)

    for i in range(Q):
        line2 = input().split()
        day  = int(line2[0])
        problem = int(line2[1])

        sum1 = sum(day_no[1:day+1])

        if(sum1 >= problem):
            print("Go Camp")
        else:
            print("Go Sleep")
