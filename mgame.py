import math
T = int(input())

for i in range(T):
    input_line = input().split()
    N = int(input_line[0])
    P = int(input_line[1])
    ans = 0
    if(N<=2):
        print(P**3)
    else:
        part_1 = ((P-math.ceil(N/2)) + 1)**2
        part_2 = (P-N) * (P-math.ceil(N/2)+1)
        part_3 = (P-N)**2
        ans = part_1+part_2+part_3
        print(ans)
