import math

last_digit = [0,1]
for i in range(2,60):
	last_digit.append((last_digit[i-1] + last_digit[i-2]) % 10)

T = int(input())

for _ in range(T):
	n = int(input())
	x = bin(n)
	x = len(x[2:])
	index = pow(2,x-1) - 1
	ans = last_digit[index % 60]
	print(ans)
