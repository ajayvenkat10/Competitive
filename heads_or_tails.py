# x,y,a,b = map(int, input().split())

# final = []
# start = a if(a > b) else b+1

# for i in range(start, x+1):
#     for j in range(b, y+1):
#         if(i > j):
#             final.append([i,j])

#         else:
#             break 

# print(len(final))
# for i in range(len(final)):
#     print(*final[i])


N = int(input())
bachelorette,bachelor = map(str, input().split())
mojito=0
rum=0

for i in bachelor:
	if i=='m':
		mojito+=1
	else:
		rum+=1

pos=0
for i in bachelorette:
	if i=='m':
		if mojito>0:
			mojito-=1
			pos+=1
		else:
			break
	else:
		if rum>0:
			rum-=1
			pos+=1
		else:
			break
		
		
print (N-pos)

