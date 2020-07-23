f = open('leapfrog_ch_.txt', "r")
x = open('leapfrog_output.txt' , "w")
t  = int(f.readline())

for j in range(t):
    n = f.readline()

    bcount = 0
    dotcount = 0

    for i in range(1,len(n)):
        if(n[i] == 'B'):
            bcount += 1

        else:
            dotcount += 1

    if(bcount==0 or dotcount==0):
        ans="N"
    elif(bcount==1 and dotcount>1):
        ans="N"
    else:
        ans="Y"

    x.write("Case #%d: %c\n" % (j+1, ans))
