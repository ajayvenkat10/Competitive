flag = True 

for i in range(8):
    row = input()

    x = row[0]
    y = row[1]

    if(x == y):
        flag &= False 

    else:
        for j in range(2,8):
            if(j%2 == 0):
                if(row[j] != x):
                    flag &= False
                    break 

            else:
                if(row[j] != y):
                    flag &= False
                    break 
    
if(flag):
    print("YES")

else:
    print("NO")