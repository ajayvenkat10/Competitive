import math

t = int(input())

for i in range(t):
    n,k = map(int, input().split())

    ans = []
    flag = True 

    if(k > n):
        flag = False 

    else:
        quotient =  n//k
        remainder = n % k

        if(remainder % 2 == 0):
            ans = [quotient] * k
            ans[0] += remainder
            flag = True

        else:
            if(k % 2 == 1):
                part1 = [quotient + remainder, quotient + k-2]
                part2 = [quotient - 1] * (k-2)
                part1.extend(part2)
                ans.extend(part1)
                if(quotient-1 <= 0):
                    flag = False

                else:
                    flag = True

            else:
                flag = False


    if(flag):
        print("YES")
        print(* ans)
        
    else:
        print("NO")