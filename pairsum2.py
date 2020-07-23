t = int(input())

for i in range(t):
    n,q = map(int, input().split())
    sum_arr = list(map(int, input().split()))

    original = [0]

    for i in range(1,n):
        original.append(sum_arr[i-1]-original[i-1])

    for i in range(q):
        l,r = map(int, input().split())
        l-=1
        r-=1

        if(abs(l-r)%2 == 1):
            print(original[l]+original[r])

        else:
            print("UNKNOWN")
