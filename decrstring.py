import math

t = int(input())
alphabetset = "zyxwvutsrqponmlkjihgfedcba"

for i in range(t):
    n = int(input())
    n+= max(math.ceil(n/25),1)
    ans= [alphabetset] * (n//26)

    ans.append(alphabetset[26 - (n%26): ])

    ans = ans[::-1]

    print(''.join(ans))
