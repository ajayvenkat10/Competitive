n=int(raw_input(""))
count=0
A=[]
for i in range(n):
    s=raw_input("")
    A.append(s)

B=["ch","he","ef","che","hef","chef"]
for i in range(len(A)):
    str=A[i]
    for i in B:
        if i in str:
            count=count+1
            break


print count
