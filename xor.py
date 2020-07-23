n=int(input(""))
Z=[]
for i in range(n):
    sum=0
    ans=0
    A=[]
    B=[]
    a=int(input(""))
    b=input("")
    b=b.split()

    for i in range(a):
        A.append(int(b[i]))
    # C=[]
    # for i in range(0,a/2):
    #     for j in range(i,a):
    #         sum=A[i]+A[j]
    #         B.append(sum)
    #         C.append(sum)
    #     # C=C[1:]
    #     B.extend(C[1:])
    #     C=[]
    #
    # for i in range(a/2,a):
    #     for j in range(i,a):
    #         sum=A[i]+A[j]
    #         B.append(sum)
    #         C.append(sum)
    #     # C=C[1:]
    #     B.extend(C[1:])
    #     C=[]
# print B

    for i in range(len(A)):
        ans=ans^A[i]
    ans= ans*2
    Z.append(ans)

for i in range(len(Z)):
    print(Z[i])
