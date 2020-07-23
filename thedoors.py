n = int(input())

zero = 0
one = 0

arr = input().split()

for i in range(n):
    if(int(arr[i]) == 0):
        zero = i+1
    else:
        one = i+1

if(zero<one):
    print(zero)
else:
    print(one)
