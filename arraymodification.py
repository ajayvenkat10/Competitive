t = int(input())

while(t):
    t-=1
    n,k =  map(int,input().split())
    arr = list(map(int,input().split()))

    if(n==1):
        print(0)

    else:
        hashmap = {}
        hashmap[0] = arr[:]

        for i in range(1,3):
            for j in range(n):
                arr[j] = arr[j] ^ arr[n-1-j]

            hashmap[i] = arr[:]

        A = []

        if((k//n) %3 == 0):
            A = hashmap[0]
            if(n%2 == 1):
                if(k>n):
                    A[n//2] = 0

        elif((k//n) %3 == 1):
            A = hashmap[1]

        else:
            A = hashmap[2]

        k = k - (n*(k//n))

        for i in range(k):
            A[i] = A[i] ^ A[n-1-i]

        print(*A)
