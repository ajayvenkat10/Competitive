t = int(input(""))

for i in range(t):
    first_line = input("")
    first_line = first_line.split()
    n = int(first_line[0])
    k = int(first_line[1])
    count = 0
    sequence = []
    array = input("")
    array = array.split()
    for i in range(n):
        sequence.append(int(array[i]))

    for i in range(len(sequence)):
        if(sequence[i]%k == 0):
            count += 1

    print(count)
