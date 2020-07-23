def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

t = int(input())

for i in range(t):
    n = int(input())
    arr = []
    count_arr = [0] * 10000003
    even = 0
    odd = 0

    for i in range(n):
        length = len(arr)
        number = int(input())

        if(count_arr[number] != 0 or number == 0):
            odd = odd
            even = even

        else:
            if(count_arr[number] == 0 and number != 0):
                arr.append(number)
                count_arr[number] += 1
                check = countSetBits(number)
                if(check % 2== 0):
                    even += 1
                else:
                    odd += 1

            for j in range(length):
                xor = number ^ arr[j]
                if(count_arr[xor] == 0 and xor != 0):
                    arr.append(xor)
                    count_arr[xor] += 1
                    check = countSetBits(xor)

                    if(check % 2== 0):
                        even += 1
                    else:
                        odd += 1

        print(even , odd)

        # if(i==0):
        #     arr.append(number)
        #     count_arr[number] += 1
        #     check = countSetBits(number)
        #     if(check % 2== 0):
        #         even += 1
        #     else:
        #         odd += 1
        #
        # else:
