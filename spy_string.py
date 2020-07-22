t = int(input())

for i in range(t):
    n,m = map(int, input().split())

    strings = []

    for i in range(n):
        word = input()
        strings.append(word)

    positions = set()

    final = list(strings[0])
    final2 = list(strings[0])
    flag = True 

    for i in range(1,n):
        x = strings[i-1]
        y = strings[i]

        for j in range(m):
            if(x[j] != y[j]):
                positions.add(j)
                if(len(positions) == 1):
                    final[j] = y[j]

                if(len(positions) == 1):
                    final2[j] = y[j]

                if(len(positions) > 2):
                    flag = False 
                    break 
        
        if(flag == False):
            break 

    if(not flag):
        print("-1")

    else:        
        
        for i in range(n):
            count = 0
            for j in range(m):
                if(strings[i][j] != final[j]):
                    count += 1

                if(count > 1):
                    flag = False 
                    break 
                    
        print(''.join(final))

