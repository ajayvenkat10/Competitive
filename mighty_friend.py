t=int(raw_input(""))
Z=[]
for i in range(t):
    score_C=0
    score_M=0
    count=0
    x=0
    C=[]
    M=[]
    A=[]
    n=raw_input("")
    n=n.split()

    N=int(n[0])
    K=int(n[1])

    a=raw_input("")
    a=a.split()
    for i in range(N):
        A.append(int(a[i]))

    for i in range(len(A)):
        if(i%2==0):
            C.append(A[i])
        else:
            M.append(A[i])

    #         print C
    # print M

    C.sort()
    M.sort()

    if(K>len(M)):
        K=len(M)

    for i in range(len(C)):
        score_C += C[i]

    for i in range(len(M)):
        score_M += M[i]


    if(score_M > score_C):
        Z.append("YES")

    else:
        if(K==0):
            Z.append("NO")

        else:
            while(K!=0):

                x=C[len(C)-1]
                C[len(C)-1]=M[0]
                M[0]=x


                C.sort()
                M.sort()

                # print C
                # print M

                score_C=0
                score_M=0

                for i in range(len(C)):
                    score_C += C[i]

                for i in range(len(M)):
                    score_M += M[i]

                # score_M = score_M - M[0] + C[len(C)-1]
                # score_C = score_C - C[len(C)-1] + M[0]

                if(score_M > score_C):
                    count=1
                    break

                K=K-1

            if(count==1):
                Z.append("YES")
            else:
                Z.append("NO")

for i in range(len(Z)):
    print Z[i]
