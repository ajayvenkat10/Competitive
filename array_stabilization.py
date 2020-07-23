n = int(input())

arr = []

array = input().split()
for i in range(n):
    arr.append(int(array[i]))

arr.sort()

p1 = arr[-1] - arr[1]
p2 = arr[-2] - arr[0]

if(p1<p2):
    print(p1)
else:
    print(p2)
