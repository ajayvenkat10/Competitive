from collections import defaultdict

def update(D, l, r, x):

	D[l] += x
	D[r + 1] -= x

def resultArray(A, D):
	for i in range(len(A)):
		if (i == 0):
			A[i] = D[i]
		else:
			A[i] = D[i] + A[i - 1]

	return(A)

t = int(input())

for i in range(t):
	n = int(input())
	C = list(map(int, input().split()))
	H = list(map(int, input().split()))
	final = [0] * n
	D = [0]* (n+1)

	for i in range(len(C)):
		start = max(0, i - C[i])
		end = min(len(C)-1, i + C[i])
		update(D,start,end,1)

	final = resultArray(final,D)
	final_dict = defaultdict(int)
	h_dict = defaultdict(int)

	flag = 1

	for i in range(len(final)):
		final_dict[final[i]] += 1
		h_dict[H[i]] += 1

	final_set = list(set(final))
	for i in range(len(final_set)):
		if(final_dict[final_set[i]] != h_dict[final_set[i]]):
			flag = 0
			break

	if(flag):
		print("YES")

	else:
		print("NO")
