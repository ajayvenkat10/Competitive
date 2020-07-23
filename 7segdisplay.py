x = [0,1,2,3,4,5,6,7,8,9]
y = [6,2,5,5,4,5,6,3,7,6]
dictionary = dict(zip(x,y))

t = int(input())

for i in range(t):
    n = input()
    number_of_sticks = 0
    for i in range(len(n)):
        number_of_sticks += dictionary[int(n[i])]

    total_of_1 = 0
    total_of_7 = 0
    if(number_of_sticks % 2 == 0):
        total_of_1 = number_of_sticks//2

    else:
        if(number_of_sticks - 3 < 0):
            total_of_7 = 0

        elif(number_of_sticks - 3 == 0):
            total_of_7 = 1

        else:
            total_of_1 = number_of_sticks//2 - 1
            total_of_7 = 1

    ans = "7" * total_of_7 + "1"*total_of_1

    print(ans)
