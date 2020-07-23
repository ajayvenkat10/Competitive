N= int(raw_input(" "))
A= []
B= []

for i in range(N):
	score=raw_input("")
	score=score.split(" ")
	p1=int(score[0])
	p2=int(score[1])
	A.append(p1)
	B.append(p2)

sum1=0
sum2=0
l1=0
l2=0
W=0
L=0
lead=0

for i in range(N):
	sum1 = sum1+A[i]
	sum2 = sum2+B[i]
	lead = sum1-sum2

	if(lead<0):
		if(abs(lead)>abs(l2)):
			l2 = abs(lead)

	if(lead>0):
		if(lead>l1):
			l1=lead

if(l1>l2):
	L=l1
	W=1
else:
	L=l2
	W=2

print ("%d %d") % (W,L)
