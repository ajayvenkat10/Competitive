t = int(input())
MAX = 1000000000000
dict = {'0': 2, '1': 2, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 8, '8': 9, '9': 10, 'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26, 'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35, 'Z': 36}

for _ in range(t):
    n = int(input())

    base,number = input().split()
    base = int(base)

    answers = set()

    if(base == -1):
        number_arr = list(number)
        for i in range(dict[max(number_arr)],37):
            converted_number = int(number,i)
            answers.add(converted_number)

    else:
        converted_number = int(number,base)
        answers.add(converted_number)

    for i in range(1,n):
        base,number = input().split()
        base = int(base)

        common = set()

        if(base == -1):
            number_arr = list(number)
            for j in range(dict[max(number)],37):
                converted_number = int(number,j)
                common.add(converted_number)

        else:
            converted_number = int(number,base)
            common.add(converted_number)

        answers = answers.intersection(common)

    answers = list(answers)

    if(len(answers)==0):
        print(-1)

    else:
        X = min(answers)
        if(X <= MAX):
            print(X)
        else:
            print(-1)
