col = raw_input("")
col = col.split(" ")
n=int(col[0])
m=int(col[1])
count=0
A=[]

books=raw_input("")
books=books.split(" ")
for i in range(n):
	a=int(books[i])
	if(a<=max):
		A.append(a)
	else:
		quit()

B=[]
j=0
i=0
operations=raw_input("")
operations= operations.split(" ")

while True:
	b1 =int(operations[i])
	B.append(b1)
	b=B[i]
	i=i+1
	if(b==0):
		break

	elif(b==2):
		if(j==n-1):
			continue
		else:
			j=j+1

	elif(b==1):
		if(j==0):
			continue
		else:
			j=j-1

	elif(b==3):
		if(A[j]==0 or count==1):
			continue
		else:
			A[j]=A[j]-1
			count=1

	elif(b==4):
		if(A[j]==m or count==0):
			continue
		else:
			A[j]=A[j]+1
			count=0

	else:
		continue

A1=[]
for i in range(len(A)):
	c=str(A[i])
	A1.append(c)

C=" ".join(A1)
print C
