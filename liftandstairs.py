line1 = input().split()

x = int(line1[0])
y = int(line1[1])
z = int(line1[2])
t1 = int(line1[3])
t2 = int(line1[4])
t3 = int(line1[5])

stairs = abs(x-y)*t1
lift =  (t3*3)+(abs(x-y)+ abs(x-z))*t2

if(stairs<lift):
    print("NO")

else:
    print("YES")
