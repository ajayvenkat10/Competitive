import math
n = int(input())
sum = 0
if(n==1):
    print("Not Perfect")
else:
    for i in range(1,int(math.sqrt(n))+1):
        if(n % i == 0):
            sum+= i
            if(n//i != n):
                sum+= n//i
                    
    if(n == sum):
        print("Perfect")
    else:
        print("Not Perfect")
