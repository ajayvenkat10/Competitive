from collections import defaultdict

encode = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
decode = [i for i in range(2,37)]
decode.insert(0,2)
mapping = dict(zip(encode,decode))

t = int(input())

for i in range(t):
    hashmap = defaultdict(set)
    n = int(input())

    for i in range(n):
        b,y = input().split()
        b = int(b)

        if(b!= -1):
            value = int(y,b)
            hashmap[i].add(value)

        else:
            y_list = list(y)
            start = mapping[max(y_list)]
            end = 37

            for j in range(start,end):
                value = int(y,j)
                hashmap[i].add(value)

    possibilities = list(hashmap.values())
    inter = hashmap[0]

    for i in range(len(possibilities)):
        inter = inter & possibilities[i]

    inter = list(inter)

    if(inter == []):
        print(-1)

    else:
        ans = min(inter)

        if(ans > 1000000000000):
            print(-1)

        else:
            print(ans)
