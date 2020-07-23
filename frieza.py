n = int(input(""))
A = ['f','r','i','e','z','a']
for i in range(n):
    a = input("")
    count = 0
    Ans = ""
    i=0
    while i < len(a):
        if a[i] in A:
            while i<len(a):
                if a[i] in A:
                    count = count+1
                    i = i+1
                else:
                    break

        else:
            while i<len(a):
                if a[i] not in A:
                    count = count+1
                    i = i+1
                else:
                    break
        Ans = Ans+str(count)
        count = 0

    print(Ans)
