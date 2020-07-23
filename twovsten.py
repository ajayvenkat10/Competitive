t=int(raw_input(""))
A=[]
B=[]
for i in range(t):
    a=int(raw_input(""))
    A.append(a)

count=0
for i in range(t):
    if(A[i]%10==0):
        B.append(0)
    elif(A[i]%5==0):
        B.append(1)
    else:
        B.append(-1)

for i in range(len(B)):
    print B[i]
