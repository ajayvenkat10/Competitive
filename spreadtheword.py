t = int(input())

for i in range(t):
    N = int(input())
    input_line = input().split()
    weight_array = []
    sum1 = 1
    count = 0

    for i in range(N):
        weight_array.append(int(input_line[i]))

    start = 0
    end = 1
    x =0
    while(sum1+1<=N):
        x = x + sum(weight_array[start:end])
        sum1 = sum1 + x
        count += 1
        # if(sum1>=N):
        #     print(count)
        #     break
        # x = sum(weight_array[:sum1])
        start = end
        end = end+x

    print(count)
