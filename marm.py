t = int(input())

for _ in range(t):
    N,K = input().split()
    N,K = int(N), int(K)
    sequence = list(map(int,input().split()))

    if(N==1):
        ans = 0
        print(ans)

    else:
        sequence1 = sequence[:]
        for i in range(len(sequence1)):
            sequence1[i] ^= sequence1[N-1-i]

        sequence2 = sequence1[:]
        for i in range(len(sequence2)):
            sequence2[i] ^= sequence2[N-1-i]

        check = K//N

        if(check %3 == 0):
            ans = sequence
            if(N%2 == 1):
                if(K>N):
                    mid = N//2
                    ans[mid] = 0

        elif(check %3 == 1):
            ans = sequence1

        else:
            ans = sequence2

        K %= N

        for i in range(K):
            ans[i] ^= ans[N-1-i]

        print(*ans)
