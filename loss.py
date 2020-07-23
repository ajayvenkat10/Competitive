n= int(raw_input(""))
A=[]
B=[]
sum1=0
total=0
mrp=0
discounted=0
loss=0
for i in range(n):
    a=int(raw_input(""))
    for i in range(a):
        x=raw_input("")
        x=x.split(" ")
        for i in range(2):
            A.append(int(x[i]))

        mrp=A[0]
        total= mrp*A[1]
        hike=total+(A[1]/100)*total
        discounted=hike-(A[1]/100)*hike
        sum1=total-discounted
        loss+=-sum1 
    B.append(loss)

for i in range(len(B)):
    print B[i]
