n=int(raw_input(""))
count=0
A=[]
a=raw_input("")
a=a.split()
for i in range(n):
    b=int(a[i])
    A.append(b)


while(len(A)>0):
    count = count + pali(A)

print count
