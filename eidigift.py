from collections import defaultdict 
t = int(input())
for i in range(t):
    a1,a2,a3,c1,c2,c3 = list(map(int, input().split()))
    arr = [(a1,c1), (a2,c2), (a3,c3)]

    arr.sort() 
    a = []
    c = []
    for i in range(len(arr)):
        a.append(arr[i][0])
        c.append(arr[i][1])

    C = c[:]
    C.sort()

    dict1 = defaultdict(int)
    dict2 = defaultdict(list)

    for i in range(3):
        dict1[a[i]] += 1
        dict2[a[i]].append(c[i])

    if(C==c):
        x = list(dict1.keys())
        flag = 0
        for i in range(len(x)):
            if(dict1[x[i]] == len(dict2[x[i]]) and len(set(dict2[x[i]]))==1 and len(set(a)) == len(set(c))):
                flag = 1

            else:
                flag = 0
                break
        if(flag):
            print("FAIR")

        else:
            print("NOT FAIR")
    
    else:
        print("NOT FAIR")



