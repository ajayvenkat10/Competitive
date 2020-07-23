input_line = input().split()
N = int(input_line[0])
M = int(input_line[1])
A = []
B = []

A_elements = input().split()
B_elements = input().split()
for i in range(N):
    A.append(int(A_elements[i]))

for i in range(M):
    B.append(int(B_elements[i]))

min_pos = A.index(min(A))
max_pos = B.index(max(B))

for i in range(len(B)):
    print(min_pos,i)

for i in range(len(A)):
    if(i!=min_pos):
        print(i,max_pos)
