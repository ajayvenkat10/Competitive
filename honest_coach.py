t = int(input())

for i in range(t):
    n = int(input())

    strength = list(map(int, input().split()))

    strength = strength[:n]
    strength.sort() 

    minimum = 1000000007

    for i in range(1,n):
        minimum = min(abs(strength[i] - strength[i-1]), minimum)

    print(minimum)