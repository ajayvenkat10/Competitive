t = int(input())

for i in range(t):
    n,k = map(int, input().split())
    seating = input()

    count = 0
    seating = list(seating)
    i = 0

    left = [-1] * n 
    right = [-1] * n

    pos = -1
    for i in range(n):
        if(seating[i] == '1'):
            pos = i
        left[i] = pos 

    pos = -1
    for i in range(n-1, -1, -1,):
        if(seating[i] == '1'):
            pos = i
        right[i] = pos 

    while(i < n):
        if(seating[i] == '0'):
            if((left[i] == -1 or (i - left[i]) > k) and (right[i] == -1 or (right[i] - i) > k)):
                count += 1
                i += k+1

            else:
                i += 1

        else:
            i += 1

    print(count)
            