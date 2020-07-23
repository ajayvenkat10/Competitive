N = int(input())
H = list(map(int, input().split()))
C = list(map(int, input().split()))

cost = 0

for i in range(1,N):
    if(H[i] > H[i-1]):
        cost += C[i-1]

print(cost)
