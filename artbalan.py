t = int(input())

for i in range(t):
    input_string = input()
    dict  = {}
    final = []
    for i in range(ord('A'),ord('Z')+1):
        dict[chr(i)] =0

    for i in range(len(input_string)):
        dict[input_string[i]] += 1

    count_arr = []
    for i in dict.values():
        count_arr.append(i)

    count_arr.sort(reverse=True)
    length = len(input_string)
    
    for i in range(1,27):
        if(length%i == 0):
            count = length//i
            operations=0
        for j in range(len(count_arr)):
            if(count_arr[j] > count):
                operations+= (count_arr[j] - count)

            else:
                operations+= sum(count_arr[i:])
                break

        final.append(operations)

    print(min(final))
