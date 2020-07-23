from collections import defaultdict

def factorial(n):
	fact = 1;
	for i in range(2,n+1):
		fact = fact*i

	return(fact)

t = int(input())

for i in range(t):
	n,k = map(int,input().split())
	arr = list(map(int, input().split()))

	arr.sort()

	x = list(set(arr))
	x.sort()

	count = defaultdict(int)

	for i in range(len(arr)):
		count[arr[i]] += 1

	total = 0
	flag = 0
	pos = -1

	if(k == n):
		ans = 1

	else:
		for i in range(len(x)):
			if(total + count[x[i]] <= k):
				if(total + count[x[i]] == k):
					flag = 0
					break
				else:
					total += count[x[i]]

			else:
				flag = 1
				pos = i
				break

		if(flag == 0):
			ans = 1

		else:
			ans = factorial(count[x[pos]]) // (factorial(count[x[pos]] - (k-total)) * factorial(k-total))

	print(ans)
