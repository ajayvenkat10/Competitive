t = int(input())

for i in range(t):
    brackets = input()

    open_brackets = []
    closed_brackets = []
    open_count = 0
    closed_count = 0
    maximum = 0

    for i in range(len(brackets)):
        if(brackets[i] == '('):
            if(closed_count > 0):
                closed_brackets.append(closed_count)
                closed_count = 0

            open_count += 1

        else:
            if(open_count  > 0):
                open_brackets.append(open_count)
                open_count = 0

            closed_count += 1

    if(closed_count > 0):
        closed_brackets.append(closed_count)
    else:
        open_brackets.append(open_count)

    # if(brackets[0] == ')'):
    #     closed_brackets = closed_brackets[1:]
    #
    # if(brackets[-1] == '('):
    #     closed_brackets = closed_brackets[:len(closed_brackets)-1]

    open = sum(open_brackets)
    close = 0
    closed_brackets = closed_brackets[::-1]
    open_brackets = open_brackets[::-1]

    for i in range(len(closed_brackets)):
        close += closed_brackets[i]
        x = min(close,open)
        if(x > maximum):
            maximum = x

        open -= open_brackets[i]

    print(maximum * 2)
