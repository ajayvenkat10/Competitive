t = int(input())

for i in range(t):
    hot,cold,exp = map(int, input().split())
    count = 1
    if(exp == hot):
        ans = 1

    elif((hot+cold)//2 == exp):
        ans = 2 

    else:
        total = hot 
        diff = 1000000
        ans_count = 0
        flag = False
        while(total <= 10000000):
            if((total/count) == exp):
                ans = count 
                flag = True
                break 

            else:
                if(abs((total/count)-exp) < diff):
                    diff = abs((total/count)-exp)
                    ans_count = count  
                
                count += 2
                total += (hot+cold)

        if(flag):
            ans = count 
        else:
            ans = ans_count

    print(ans)