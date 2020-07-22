from collections import defaultdict

t = int(input())

while (t>0):

    n = int(input())
    A = input()
    B = input()

    if(len(set(A) & set(B)) != len(set(B))):
        print(-1)

    else:
        positions = defaultdict(list)
        diff_positions = defaultdict(list)
        
        valid = True

        for i in range(n):
            if(A[i] != B[i]):        
                if(A[i] > B[i]):
                    diff_positions[B[i]].append(i)
                    
                else:
                    valid = False 
                    break 

            positions[A[i]].append(i)

        if(valid):
            alphas = list(diff_positions.keys())
            alphas.sort()
            
            print(len(alphas))

            for i in range(len(alphas)-1,-1,-1):
                ans = diff_positions[alphas[i]]
                index = positions[alphas[i]]
                ans.insert(0,index[0])
                ans.sort()
                ans.insert(0, len(ans))
                print(*ans)

        else:
            print(-1)

    t-=1