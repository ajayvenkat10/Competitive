t = int(input(""))

for i in range(t):
    s = input("")
    count = 0

    replace = min(s)

    ,
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if(s[i]<s[j]):
                count+=1
