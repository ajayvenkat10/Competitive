n= raw_input("")
n=n.split(" ")
N=int(n[0])
K=int(n[1])
A=[]
B=[]

for i in range(2,N+2):
    a=int(n[i])
    A.append(a)

for i in range(N+2,len(n)):
    b=int(n[i])
    B.append(b)

print A
print B
