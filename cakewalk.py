import math

t = int(input())

for i in range(t):
    n = int(input())

    if(n%10 != 0):
        ans = "No"

    else:
        if(math.log10(n) == int(math.log10(n))):
            ans = "Yes"

        else:
            x = len(str(n))
            n = int(''.join(reversed(str(n))))
            n = int(''.join(reversed(str(n))))
            
            if(math.log2(n) == int(math.log2(n))):
                if(x >= len(str(n)) + int(math.log2(n))):
                    ans = "Yes"

                else:
                    ans = "No"

            else:
                ans = "No"

    print(ans)
