def solve (S,n):
    # Your Code Here
    arr = []
    for i in range(len(S)-1):
        count = 0
        for j in range(i+1,len(S)):
            if(S[i] > S[j]):
                count += 1

            else:
                break

        arr.append(count)

    arr.append(0)

    return arr

T = int(input())
for _ in range(T):
    n = int(input())
    S = list(map(int, input().split()))

    out_ = solve(S,n)
    print(*out_)
