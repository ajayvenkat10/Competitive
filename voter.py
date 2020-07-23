n1= int(raw_input("enter the number of voter ID's in the first list: "))
A=[]
print "Enter the voter ID's fo list 1: "
for i in range(n1):
    a=int(raw_input(" "))
    A.append(a)

n2= int(raw_input("enter the number of voter ID's in the second list: "))
B=[]
print "Enter the voter ID's fo list 2: "
for i in range(n2):
    b=int(raw_input(" "))
    B.append(b)

n3= int(raw_input("enter the number of voter ID's in the third list: "))
C=[]
print "Enter the voter ID's fo list 3: "
for i in range(n3):
    c=int(raw_input(" "))
    C.append(c)

d=set(A)
e=set(B)
f=set(C)

j=set(d.intersection(e))
k=set(e.intersection(f))
l=set(f.intersection(d))

m= j.union(k.union(l))
print m
m=list(m)

for i in range(len(m)):
    for j in range(len(m)):
        if(m[j]>m[j+1]):
            temp=m[j]
            m[j]=m[j+1]
            m[j+1]=temp

print m
