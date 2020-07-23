n=int(raw_input(""))
count=0
A=[]
a=raw_input("")
a=a.split()
for i in range(n):
    b=int(a[i])
    A.append(b)
B=A
C=[]
count=0
while(len(A)>0):
    i=0
    j=len(A)-1
    k=len(A)-1

    while(i<=j):
        if(i==j):
            count=count+1
            if(i==0):
                k=i
            A=B[k+1:]
            B=A
            break

        else:
            if(A[i]==A[j]):
                C=A[i:j+1]
                if C==C[::-1]:
                    count=count+1
                    A=A[j+1:]
                    print A
                    break
                # i=i+1
                else:
                    # k=j
                    A=A[0:j]
                    print A
                    break
                # j=j-1
            else:
                A=A[0:j]
                print A
                break

print count
