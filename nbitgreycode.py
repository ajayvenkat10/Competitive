from collections import defaultdict

def calculate(n):

	if (n <= 0):
		return

	bits_arr = []

	bits_arr.append("0")
	bits_arr.append("1")

	i = 2
	j = 0
	while(True):

		if i >= 1 << n:
			break

		for j in range(i - 1, -1, -1):
			bits_arr.append(bits_arr[j])

		for j in range(i):
			bits_arr[j] = "0" + bits_arr[j]

		for j in range(i, 2 * i):
			bits_arr[j] = "1" + bits_arr[j]

		i <<= 1

	for i in range(len(bits_arr)):
		bits_arr[i] = int(bits_arr[i],2)

	return(bits_arr)

generateGraybits_arr(2)
