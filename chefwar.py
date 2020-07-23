t = int(input())

for i in range(t):
    n = int(input())
    defence_power = list(map(int, input().split()))
    fire_power = int(input())
    arr = defence_power[:]
    power = []
    position = []
    flag = 1
    for i in range(len(defence_power) + 1):
        arr.insert(i,"Josh")

        sum = 0
        j = 0
        num = 0
        while(len(arr) > 2):
            if(arr[0] == "Josh" and num == 0):
                j = 1

            if(arr[j%len(arr)] == "Josh"):
                sum += arr[(j-1)%len(arr)]
                j = (j+1)%len(arr)

            else:
                if(arr[(j+1)%len(arr)] != "Josh"):
                    arr.pop((j+1)%len(arr))
                j = (j+1)% len(arr)

            num += 1

        arr.remove("Josh")

        if(arr[0] <= fire_power):
            sum += fire_power
            power.append(sum)
            position.append(i)

        arr = defence_power[:]

    if(len(power) == 0):
        print("impossible")

    else:
        minimum = 100000000009
        pos = -1
        for i in range(len(power)):
            if(power[i] < minimum):
                minimum = power[i]
                pos = position[i]

        print("possible")
        print(pos+1 , minimum)
