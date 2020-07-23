t = int(input())

def ovlp(l, r, x, y):
    return (y >= l and x <= l) or (x <= r and y >=r)



while t:
    n = int(input())
    segs = []
    for i in range(n):
        lis = [int(x) for x in input().split()]
        segs.append(lis)

    d = False
    for i in range(n):
        if d:
            break
        cov = 0
        for j in range(n):
            if ovlp(segs[i][0], segs[i][1],segs[j][0], segs[j][1] ):
                if segs[i][2] == segs[j][2]:
                    cov += 1
            if cov > 2:
                print("NO")
                d = True
                break
    if not d:
        print("YES")

    t-=1
