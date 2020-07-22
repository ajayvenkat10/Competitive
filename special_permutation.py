t = int(input())

for _ in range(t):
    n = int(input())

    if(n == 2 or n == 3):
        print(-1)

    else:
        odd = []
        even = []
        for i in range(n,0,-1):
            if(i%2 == 0):
                even.append(i)
            else:
                odd.append(i)

        even.sort()
        odd.append(4)
        odd.append(2)
        odd.extend(even[2:])
        print(* odd)