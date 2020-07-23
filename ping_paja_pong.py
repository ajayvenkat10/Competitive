import math
t = int(input())

for i in range(t):
    x,y,k = map(int,input().split())

    if(math.ceil((x+y+1)/k)%2 == 0):
        print("Paja")

    else:
        print("Chef")
