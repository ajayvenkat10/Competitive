arr = []
n,m = map(int,input().split())
# print(n,m)
# for i in range(n):
# 	arr.append(map(int,input().split()))
# print(arr)

left,right,up,down = [],[],[],[]
temp = []
for j in range(m):
	temp.append(0)
for i in range(n):
	left.append(temp)
	right.append(temp)
	up.append(temp)
	down.append(temp)

print(left)
print(right)
print(up)
print(down)
