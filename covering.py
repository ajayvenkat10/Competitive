n = int(input())

interval = []

for i in range(n):
    line = input().split()
    start,end = int(line[0]),int(line[1])
    interval.append((start,end))

interval.sort()

min_start = interval[0][0]
min_end = interval[0][1]

ans = 1

for i in range(1,n):
    if(interval[i][0] > min_end):
        min_start = interval[i][0]
        min_end = interval[i][1]
        ans += 1

    elif(interval[i][1] <= min_end):
        min_start = interval[i][0]
        min_end = interval[i][1]

print(ans)
