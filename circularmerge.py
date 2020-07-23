t  = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    while(len(arr) > 2):
        minimum = 2000000009
        for i in range(len(arr)-1):
            x = arr[i] + arr[i+1]
            if(x < minimum):
                minimum = x
                position1 = i
                position2 = i+1

        if(arr[0] + arr[-1] < minimum):
            minimum = arr[0] + arr[-1]
            position1 = 0
            position2 = -1

        if(position2 != -1):
            position2 = position2 - 1

        del(arr[position1],arr[position2])

        arr.insert(position1,minimum)
        answer += minimum

    if(len(arr) <= 2):
        answer += sum(arr)

    print(answer)
