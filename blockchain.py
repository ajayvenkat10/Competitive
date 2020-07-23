def wordcount(filename, searchword):
    count=0
    file=open(filename,"r")
    read= file.readlines()
    file.close()

    for word in searchword:
        for sentence in read:
            line=sentence.split()
            for each in line:
                if(word==each):
                    count+=1
                else:
                    count=0
    if(count>0):
        return 1
    else:
        return 0


n=int(raw_input(""))
A=[]
f= open("database.txt","a+")
for i in range (n):
    a=raw_input("")
    if(i==0):
        hashcode= hash(a)
        x= wordcount("database.txt",str(hashcode))
        if(x):
            print "Present"
        else:
            A.append(hashcode)

    else:
        b={A[i-1],a}
        hashcode= hash(tuple(b))
        x= wordcount("database.txt",str(hashcode))
        if(x):
            print "Present"
        else:
            A.append(hashcode)


for i in range(len(A)):
    f.write("%s \n" %str(A[i]))

f.close()
