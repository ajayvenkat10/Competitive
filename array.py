t = int(input())

arr = list(map(int, input().split()))

less = []
great = []
zero = []

for i in range(t):
    if(arr[i] == 0):
        zero.append(0)

    else:
        if(arr[i] < 0):
            if(len(less) == 0):
                less.append(arr[i])
            else:
                great.append(arr[i])

        else:
            great.append(arr[i])

pos = -1
count = 0
for i in range(len(great)):
    if(great[i] < 0):
        pos = i 
        count += 1

if(count % 2 == 1):
    x = great[pos]
    del(great[pos])
    zero.append(x)

print(len(less), *less)
print(len(great), *great)
print(len(zero), *zero)

