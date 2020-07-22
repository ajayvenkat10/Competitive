t = int(input())

for i in range(t):
    n,m,x,y = map(int, input().split())

    final_cost = 0
    for i in range(n):
        line = input()
        
        count = 0
        for i in range(m):
            if(line[i] == '*'):
                if(count > 0):
                    if(x <= y):
                        if(2*x <= y):
                            final_cost += (x*count)

                        else:
                            if(count % 2 == 0):
                                final_cost += y * (count//2)

                            else:
                                final_cost += (y * (count//2)) + x                                     
                    else:
                        if(count % 2 == 1):
                           final_cost += (y * (count//2)) + x
                        else:
                            final_cost += (y * (count//2))
                count = 0

            else:
                count += 1

        if(count > 0):
            if(x <= y):
                if(2*x <= y):
                    final_cost += (x*count)

                else:
                    if(count % 2 == 0):
                        final_cost += y * (count//2)

                    else:
                        final_cost += (y * (count//2)) + x                                     
            else:
                if(count % 2 == 1):
                    final_cost += (y * (count//2)) + x
                else:
                    final_cost += (y * (count//2))
        
    print(final_cost)

