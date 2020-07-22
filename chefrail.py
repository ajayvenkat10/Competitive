from collections import defaultdict
import math

factors_arr = []
def generateDivisors(curIndex, curDivisor, arr): 
	
	# Base case i.e. we do not have more 
	# primeFactors to include 
	if (curIndex == len(arr)): 
		factors_arr.append(curDivisor)
		return
	
	for i in range(arr[curIndex][0] + 1): 
		generateDivisors(curIndex + 1, curDivisor, arr) 
		curDivisor *= arr[curIndex][1] 
	
# Function to find the divisors of n 
def findDivisors(n): 
	
	# To store the prime factors along 
	# with their highest power 
	arr = [] 
	
	# Finding prime factorization of n 
	i = 2
	while(i * i <= n): 
		if (n % i == 0): 
			count = 0
			while (n % i == 0): 
				n //= i 
				count += 1
				
			# For every prime factor we are storing 
			# count of it's occurenceand itself. 
			arr.append([count, i]) 
	
	# If n is prime 
	if (n > 1): 
		arr.append([1, n]) 
	
	curIndex = 0
	curDivisor = 1
	
	# Generate all the divisors 
	generateDivisors(curIndex, curDivisor, arr) 


t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    x_axis = defaultdict(bool)
    y_axis = defaultdict(bool)

    valid = 0
    positive_x = []
    positive_y = []
    negative_x = []
    negative_y = []
    zero = False
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_axis_elements = set()
    y_axis_elements = set()
    
    for i in range(n):
        if(x[i] == 0):
            zero = True

        else:
            element = x[i]
            if(x[i]>0):
                positive_x.append(x[i])
            elif(x[i]<0):
                negative_x.append(x[i])
                element = -x[i]
        
            x_axis[element] += 1
            x_axis_elements.add(element)

    for i in range(m):
        if(y[i] == 0):
            zero = True

        else:
            element = y[i]
            if(y[i]>0):
                positive_y.append(y[i])
            elif(x[i]<0):
                negative_y.append(y[i])
                element = -x[i]
        
            y_axis[element] += 1
            y_axis_elements.add(element)
    # for i in range(m):
    #     if(y[i]>0):
    #         positive_y.append(y[i])
    #         element = y[i]
    #     elif(y[i]<0):
    #         negative_y.append(y[i])
    #         element = -y[i]
    #     else:
    #         zero = True
    #     y_axis[element] += 1


    if(zero):
        valid += (len(positive_x)+len(negative_x)) * (len(positive_y)+len(negative_y))


    x_axis_elements = list(x_axis_elements)
    y_axis_elements = list(y_axis_elements)

    for i in range(len(y_axis_elements)):
        
        factors_arr = [] 
        findDivisors(y_axis_elements[i]) 
        factors_arr.sort()

        for j in range(math.ceil(len(factors_arr)/2)):
            x1 = factors_arr[j]
            x2 = y_axis_elements[i]//factors_arr[j]

            inter = 0
            if((x_axis[x1] and x_axis[-x2]) > 0):
                inter += 1

            if((x_axis[-x1] and x_axis[x2]) > 0):
                inter += 1

            inter += inter * y_axis[y_axis_elements[i]]

            valid += inter
            inter = 0

    for i in range(len(x_axis_elements)):
        
        factors_arr = [] 
        findDivisors(x_axis_elements[i]) 
        factors_arr.sort()

        for j in range(math.ceil(len(factors_arr)/2)):
            y1 = factors_arr[j]
            y2 = x_axis_elements[i]//factors_arr[j]

            inter = 0
            if((y_axis[y1] and y_axis[-y2]) > 0):
                inter += 1

            if((y_axis[-y1] and y_axis[y2])> 0):
                inter += 1

            inter += inter * x_axis[x_axis_elements[i]]

            valid += inter
            inter = 0

    print(valid)

    # for i in range(len(positive_y)):
    #     for j in range(len(negative_y)):
    #         unknown_x = math.sqrt((pow((positive_y[i] - negative_y[j]),2) - (pow(positive_y[i],2) + pow(negative_y[j],2)))/2)
    #         valid += x_axis[unknown_x]
    #         valid += x_axis[-unknown_x]

    # for i in range(len(positive_x)):
    #     for j in range(len(negative_x)):
    #         unknown_y = math.sqrt((pow((positive_x[i] - negative_x[j]),2) - (pow(positive_x[i],2) + pow(negative_x[j],2)))/2)
    #         valid += y_axis[unknown_y]
    #         valid += y_axis[-unknown_y]

