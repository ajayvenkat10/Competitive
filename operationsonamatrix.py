t = int(input())

for _ in range(t):
    n,m,q = map(int,input().split())

    rows = [0]*n
    columns = [0]*m

    while(q):
        q-=1
        r,c = map(int,input().split())

        rows[r-1]+=1
        columns[c-1]+=1

    even = 0
    odd = 0

    for i in range(len(columns)):
        if(columns[i] % 2 == 0):
            even += 1
        else:
            odd += 1

    count = 0

    for i in range(len(rows)):
        if(rows[i]%2 == 0):
            count += odd
        else:
            count += even

    print(count)
