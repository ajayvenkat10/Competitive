import math
from collections import defaultdict

t = int(input())

for _ in range(1,t+1):
    n,m,q = map(int, input().split())
    torn_pages = list(map(int, input().split()))

    queries  = list(map(int, input().split()))

    hashmap = defaultdict(int)

    for j in range(m):
        number  = torn_pages[j]

        for i in range(1,int(math.sqrt(number))+1):
            if (number % i == 0) :
                if (number // i == i) :
                    hashmap[i] += 1

                else :
                    hashmap[i] += 1
                    hashmap[number//i] += 1

    ans = 0
    for i in range(q):
        ans += ((n//queries[i]) - hashmap[queries[i]])

    print("Case #%d: %d" % (_,ans))
