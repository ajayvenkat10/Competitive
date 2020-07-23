t = int(input())

for i in range(t):
    line1 = input().split()
    N = int(line1[0])
    K = int(line1[1])
    x = 0
    count = 0
    scores = []
    line2 = input().split()
    for i in range(N):
        scores.append(int(line2[i]))

    scores.sort(reverse=True)

    x = scores[K-1]
    for i in range(N):
        if(scores[i]>=scores[K-1]):
            count+=1

    print (count)
