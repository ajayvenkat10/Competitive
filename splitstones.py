t = int(input(""))

for i in range(t):
    input_line = input("")
    input_line = input_line.split()
    initial_sack = []
    final_sack = []
    for i in range(3):
        initial_sack.append(int(input_line[i]))

    final_sack.append(int(input_line[3]))
    final_sack.append(int(input_line[4]))

    if(sum(initial_sack) == sum(final_sack)):
        print("YES")

    else:
        print("NO")
