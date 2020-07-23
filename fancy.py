T = int(input())
for i in range(T):
    answer  = False
    input_line = input()
    input_line = input_line.split()

    for i in range(len(input_line)):
        if(input_line[i].lower() == "not"):
            answer = True
            break
    if(answer):
        print("Real Fancy")
    else:
        print("regularly fancy")
