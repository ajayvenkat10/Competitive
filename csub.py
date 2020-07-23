t = int(input())

for i in range(t):
    n = int(input())
    line = input()
    line = list(line)
    count = 0
    for i in range(n):
        if(int(line[i]) == 1):
            count += 1

    print((count * (count+1))//2)
