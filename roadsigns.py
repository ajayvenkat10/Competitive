T = int(input())
MAX = 1000000007
for i in range(0,T):
    K = int(input())

    answer = pow(2,K-1,MAX)*10

    print(answer % MAX)
