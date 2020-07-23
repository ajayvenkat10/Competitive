n = int(input())
arr = list(map(int, input().split()))

sum_of_arr = sum(arr)

prefix_sum = 0
total = 0
count = 0

if(sum_of_arr%3):
    print(0)

else:
    for i in range(n-1):
        prefix_sum += arr[i]

        if(prefix_sum == 2*(sum_of_arr//3)):
            total += count

        if(prefix_sum == sum_of_arr//3):
            count += 1


    print(total)
