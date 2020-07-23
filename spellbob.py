t = int(input(""))

for i in range(t):
    front = input("")
    back = input("")

    final = []

    for i in range(3):
        final.append(list(set(front[i]+back[i])))

    count_array_of_b = []
    count_array_of_o = []

    for i in range(len(final)):
        count_array_of_b.append(final[i].count("b"))
        count_array_of_o.append(final[i].count("o"))

    ans = True
    for i in range(3):
        if(count_array_of_b[i] == count_array_of_o[i] == 0):
            ans = False
            break

    if(count_array_of_b.count(0) > 1 or count_array_of_o.count(0) > 2):
        ans = ans and False

    else:
        ans = ans and True

    if(ans):
        print("yes")

    else:
        print("no")
