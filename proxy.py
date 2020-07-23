import math
T = int(input())

while(T):
    T -= 1
    present,absent = 0,0

    days = int(input())
    at_string = input()

    for i in range(len(at_string)):
        if(at_string[i] == 'P'):
            present += 1

    if(days<=4):
        if(present/days >= 0.75):
            answer = 0
        else:
            answer = -1

    else:
        if(present/days >= 0.75):
            answer = 0

        else:
            for i in range(2,len(at_string)-2):
                if(at_string[i] == 'A'):
                    if(at_string[i-1] == 'P' or at_string[i-2] == 'P') and (at_string[i+1] == 'P' or at_string[i+2] == 'P'):
                        absent += 1

            minimum_attendance = math.ceil(0.75 * days)
            valid_check = minimum_attendance-present

            if(valid_check <= absent):
                answer = valid_check

            else:
                answer = -1

    print(answer)
