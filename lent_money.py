t = int(input())

for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	k = int(input())
	x = int(input())
	sum1 = 0
	sum2 = 0

	if(n == k):
		sum1 = sum(arr)
		for i in range(n):
			sum2 += (arr[i] ^ x)
		ans = max(sum1, sum2)

	elif(k % 2 == 1):
		for i in range(n):
			sum1 += max(arr[i],(arr[i] ^ x))
		ans = sum1

	else:
		differnece_arr = []
		for i in range(n):
			differnece_arr.append((arr[i] ^ x) - arr[i])
		differnece_arr.sort(reverse = True)
		sum1 = sum(arr)
		greatest = 0
		difference = 0
		for i in range(n):
			difference += differnece_arr[i]
			if(i % 2 == 1 and difference > greatest):
				greatest = difference
		ans = sum1 + greatest

	print(ans)
