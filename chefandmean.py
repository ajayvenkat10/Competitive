t = int(input())

for i in range(t):
    n = int(input())
    savings = list(map(int, input().split()))
    mean = sum(savings)/n
    answer = 0
    for i in range(n):
        if(savings[i] == mean):
            answer = i+1
            break

    if(answer):
        print(answer)
    else:
        print("Impossible")
