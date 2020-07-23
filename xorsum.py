import math
from collections import defaultdict
MAX = 1000000007
def solve(A):
    main_dict = defaultdict(int)
    for i in range(len(A)):
        flag = 1
        x = A[i]
        for i in range(2,int(math.sqrt(x)) + 1):
            if(x%i == 0):
                flag = 0
                break

        if(flag == 1 and x!=1):
            main_dict[x] += 1

    MAX = 1000000007
    key = list(main_dict.keys())

    product = 1

    for i in range(len(key)):
        mid = pow(2,((len(A)-1)* main_dict[key[i]]) % MAX,MAX)
        print((len(A)-1)* main_dict[key[i]])
        product = product * pow(key[i],mid)

    return(product % MAX)

A = [1,2,2,3,1,5,5,8,8,8]
print(solve(A))
