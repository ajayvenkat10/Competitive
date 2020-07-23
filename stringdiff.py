n = int(input())

first = input()
second = input()

difference_arr = []

for i in range(n):
    difference_arr.append(abs(ord(first[i]) - ord(second[i])))

t = int(input())

for i in range(t):
    max_sum = int(input())

    size = 0
    sum1 = 0
    sub_size = 0

    for i in range(len(difference_arr)):
        if(sum1 + difference_arr[i] <= max_sum):
            sum1 += difference_arr[i]
            size += 1

        else:
            sum1 -= difference_arr[i-size]
            sum1 += difference_arr[i]

        sub_size = max(size,sub_size)

    print(sub_size)
