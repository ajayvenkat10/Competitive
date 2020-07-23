line = input().split()

cash = int(line[0])
pizza_cost = int(line[1])

arr = []
sum = 0
arjun = 0
sara = 0
cost = (cash//pizza_cost)*6

line1 = input().split()
i=0

for i in range(len(line1)):
    if(i%2==0):
        arjun+= int(line1[i])

    else:
        sara+=int(line1[i])

if(arjun>sara):
    print("Arjun")

else:
    print("Sara")
