T = int(input())

for i in range(T):
    input_line = input()
    input_line = input_line.split()
    N= int(input_line[0])
    a = int(input_line[1])
    b = int(input_line[2])

    a_count = 0
    b_count = 0
    common_count = 0

    A = input()
    A = A.split()
    for i in range(N):
        if(int(A[i])%a==0 and int(A[i])%b==0):
            common_count += 1

        elif(int(A[i])%a==0):
            a_count += 1

        elif(int(A[i])%b==0):
            b_count += 1

    if(a == b):
        if(common_count>0):
            print("BOB")
        else:
            print("ALICE")
    else:
        if(common_count>0):
            a_count += 1
        if(a_count == b_count):
            print("ALICE")
        elif(a_count > b_count):
            print("BOB")
        else:
            print("ALICE")
