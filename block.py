n=int(raw_input(""))
A=[]
for i in range (n):
    a=raw_input("")
    hashcode = hash(a)
    A.append(hashcode)

print A
