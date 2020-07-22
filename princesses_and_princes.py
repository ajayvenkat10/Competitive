from collections import defaultdict

t = int(input())

for i in range(t):
    n = int(input())
    visited = defaultdict(bool)

    arr = []
    input_set = set()
    set_size = len(input_set)
    pos = 1000000
    maxi = 0
    for i in range(n):
        flag = True
        contents = list(map(int, input().split()))
        x = contents[0]
        for j in range(1, x+1):
            input_set.add(contents[j])
            if(len(input_set) > set_size):
                set_size = len(input_set)
                flag = False
                break
                
        if(flag):
            pos = min(pos, i) 

    # ans = "OPTIMAL"
    

    main_set = set()

    for i in range(1, n+1):
        main_set.add(i)

    # sets = set()

    # for i in range(n):
    #     x = arr[i].difference(sets)
    #     if(len(x) > 0):
    #         sets.add(list(x)[0])

    #     else:
    #         pos = min(pos, i+1)

    if(len(input_set) == n):
        print("OPTIMAL")

    else:
        print("IMPROVE")
        maxi = list(main_set.difference(input_set))[0]
        print(pos + 1, maxi)
