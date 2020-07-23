t = int(input())

for i in range(t):
    line = input().split()

    a = int(line[0])
    b = int(line[1])

    if(a%2==0 or b%2==0):
        print("YES")

    else:
        print("NO")
